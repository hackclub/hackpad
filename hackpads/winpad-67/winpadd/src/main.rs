use log::{info, error};
use hidapi::{HidApi, HidError};
use std::{process::ExitCode, error::Error, fmt, thread::sleep, time::Duration, process::Command, mem::transmute};
use env_logger::{Builder as LogBuilder, Env};
use ddc::Ddc;
use mccs_caps::parse_capabilities;
use ddc_i2c::from_i2c_device;

#[derive(Debug, Copy, Clone, Eq, PartialEq, Ord, PartialOrd)]
#[allow(dead_code)]
enum WinpadKeycodes {
    BrightUp,
    BrightDown,
    BrightDefault,
    NextMonitor,
    DP1,
    DP2,
    HDMI1,
    HDMI2,
    VGA1,
    DVI1
}

impl WinpadKeycodes {
    fn to_ddc_input_source(&self) -> Option<u8> {
        // taken from mccs spec
        match self {
            Self::DP1 => Some(0x0f),
            Self::DP2 => Some(0x10),
            Self::HDMI1 => Some(0x11),
            Self::HDMI2 => Some(0x12),
            Self::VGA1 => Some(0x01),
            Self::DVI1 => Some(0x03),
            _ => None
        }
    }
}

impl TryFrom<&[u8; RAW_HID_MSG_LENGTH]> for WinpadKeycodes {
    fn try_from(value: &[u8; RAW_HID_MSG_LENGTH]) -> Result<Self, Self::Error> {
        let val = value[0];
        // check bounds
        if val >= WinpadKeycodes::BrightUp as u8 && val <= WinpadKeycodes::DVI1 as u8 {
            Ok(unsafe { transmute(val) })
        } else {
            Err(WinpaddError::InvalidHidCommand(val))
        }
    }

    type Error = WinpaddError;
}

#[derive(Debug, Clone)]
#[allow(dead_code)]
enum WinpadHostMessage<'a> {
    SwayTitle(&'a str),
    MonitorStatus {
        brightness: u8,
        input_source: u8,
        monitor_name: &'a str
    }
}

impl<'a> Into<[u8; RAW_HID_MSG_LENGTH]> for WinpadHostMessage<'a> {
    fn into(self) -> [u8; RAW_HID_MSG_LENGTH] {
        let mut buf = [0; RAW_HID_MSG_LENGTH];
        match self {
            Self::SwayTitle(s) => {
                buf[0] = 0;
                // 1 byte for msg type, 1 for null term
                let bytes_to_copy = (RAW_HID_MSG_LENGTH - 2).min(s.len());
                buf[1..1 + bytes_to_copy].copy_from_slice(s.as_bytes());
            },
            Self::MonitorStatus { brightness, input_source, monitor_name } => {
                buf[0] = 1;
                buf[1] = brightness;
                buf[2] = input_source;
                // 3 bytes for msg type/brightness/input, 1 for null term
                let bytes_to_copy = (RAW_HID_MSG_LENGTH - 4).min(monitor_name.len());
                buf[3..3 + bytes_to_copy].copy_from_slice(monitor_name.as_bytes());
            }
        }
        buf
    }
}

#[derive(Debug, Copy, Clone)]
enum WinpaddError {
    NoMonitors,
    InvalidHidCommand(u8),
}

impl fmt::Display for WinpaddError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::NoMonitors => write!(f, "No monitors found!"),
            Self::InvalidHidCommand(c) => write!(f, "Invalid hid command: {:02x}", c),
            //Self::DdcError => write!(f, "DDC transmission error")
        }
    }
}

impl Error for WinpaddError {}

const WINPAD_VID: u16 = 0xfeed;
const WINPAD_PID: u16 = 0x534b;
const WINPAD_USAGE_ID: u16 = 0x61;
const VCP_BRIGHTNESS: u8 = 0x10;
const VCP_INPUT: u8 = 0x60;
const RAW_HID_MSG_LENGTH: usize = 32;
const DEFAULT_BRIGHTNESS: u8 = 20;

#[derive(Debug, Clone)]
struct Caps {
    brightness: bool,
    input_source: Vec<u8>
}

#[derive(Debug, Clone)]
struct Monitor<T>
where T: Ddc
{
    name: String,
    capabilities: Caps,
    ddc: T
}

// For some reason, ddcutil is way better at this than the rust implementation
fn detect_monitors() -> Vec<Monitor<impl Ddc>> {
    for i in 0..7 {
        sleep(Duration::from_millis(4_u64.pow(i)));

        if let Ok(result) = Command::new("ddcutil")
            .arg("detect")
            .arg("--terse")
            .output()
        {
            if result.status.success() {
                // parse output
                let out = String::from_utf8(result.stdout).unwrap();
                return out.split("\n\n").filter_map(|d| {
                    let mut lines = d.lines();
                    // parse path and name out of output
                    let i2c_line = lines.nth(1)?;
                    let i2c_file = i2c_line.split_whitespace().last()?;

                    let caps = get_capabilities(i2c_file)?;
                    let caps = parse_capabilities(caps).ok()?;

                    // get the name from the ddcutil output or from the caps string
                    let name = lines.nth(1)
                        .and_then(|l| l.split(':').nth_back(1))
                        .map(|v| v.into())
                        .or(caps.model)
                        .unwrap_or_else(|| "Unknown".into());

                    let caps = Caps {
                        brightness: caps.vcp_features.contains_key(&VCP_BRIGHTNESS),
                        input_source: caps.vcp_features.get(&VCP_INPUT)
                            .map(|v| v.values.keys().copied().collect())
                            .unwrap_or_else(|| vec![])
                    };
                    

                    Some(Monitor {
                        capabilities: caps,
                        name,
                        ddc: from_i2c_device(i2c_file).ok()?
                    })
                }).collect();
            }
        }
    }
    vec![]
}

fn get_capabilities(i2c_file: &str) -> Option<String> {
    let bus_num = i2c_file.split_once('-')?.1;
    for i in 0..7 {
        sleep(Duration::from_millis(4_u64.pow(i)));

        if let Ok(result) = Command::new("ddcutil")
            .arg("capabilities")
            .arg("--terse")
            .arg("--bus")
            .arg(bus_num)
            .output()
        {
            if result.status.success() {
                // parse output
                let out = String::from_utf8(result.stdout).unwrap();
                if let Some(caps_start) = out.find('(') {
                    return Some(out[caps_start..].trim().into());
                }
            }
        }
    }
    None
}

fn run() -> Result<(), Box<dyn Error>> {
    info!("loading monitors...");
    
    // find monitors
    let mut monitors: Vec<_> = detect_monitors();

    if monitors.len() == 0 {
        Err(WinpaddError::NoMonitors)?;
    }
    
    let mut current_monitor = 0;

    info!("found {} monitors", monitors.len());

    let mut hid = HidApi::new()?;
    let mut hid_buf = [0; RAW_HID_MSG_LENGTH];

    loop {
        hid.reset_devices()?;
        hid.add_devices(WINPAD_VID, WINPAD_PID)?;

        // find the raw hid device
        // https://docs.qmk.fm/features/rawhid#basic-configuration
        if let Some(winpad) = hid.device_list()
            .find(|v| v.usage() == WINPAD_USAGE_ID)
            .and_then(|d| d.open_device(&hid).ok())
        {
            info!("winpad connected");
            loop {
                match winpad.read(&mut hid_buf) {
                    Err(HidError::HidApiError { .. }) => {
                        // disconnect
                        break;
                    },
                    e @ Err(_) => {
                        e?;
                    },
                    Ok(_) => {
                        let command: WinpadKeycodes = (&hid_buf).try_into()?;
                        if command == WinpadKeycodes::NextMonitor {
                            current_monitor = (current_monitor + 1) % monitors.len();
                        }
                        let mon = &mut monitors[current_monitor];
                        // ignore ddc transmission errors
                        let Ok(mut brightness) = mon.ddc.get_vcp_feature(VCP_BRIGHTNESS).map(|v| v.value() as u8) else {
                            continue;
                        };
                        let Ok(mut input_source) = mon.ddc.get_vcp_feature(VCP_INPUT).map(|v| v.value() as u8) else {
                            continue;
                        };
                        if mon.capabilities.brightness {
                            let new_brightness = match command {
                                WinpadKeycodes::BrightDefault => DEFAULT_BRIGHTNESS,
                                WinpadKeycodes::BrightUp => (brightness + 5).min(100),
                                WinpadKeycodes::BrightDown => brightness.saturating_sub(5),
                                _ => brightness
                            };

                            // set brightness
                            if new_brightness != brightness {
                                brightness = new_brightness;
                                let _ = mon.ddc.set_vcp_feature(VCP_BRIGHTNESS, brightness as u16);
                            }
                        }

                        if let Some(new_input) = command.to_ddc_input_source() {
                            if mon.capabilities.input_source.contains(&new_input) {
                                // appply this input
                                input_source = new_input;
                                let _ = mon.ddc.set_vcp_feature(VCP_INPUT, input_source as u16);
                            }
                        }

                        // report back to winpad
                        let msg = WinpadHostMessage::MonitorStatus {
                            brightness,
                            input_source,
                            monitor_name: &mon.name
                        };
                        let raw_msg: [u8; RAW_HID_MSG_LENGTH] = msg.into();
                        winpad.write(&raw_msg)?;
                    }
                }
            }
            info!("winpad disconnected");
        }

        sleep(Duration::from_secs(10));
    }
}

fn main() -> ExitCode {
    LogBuilder::from_env(Env::new().filter_or("RUST_LOG", "info")).init();
    
    // log any errors
    if let Err(err) = run() {
        error!("{}", err);
        ExitCode::FAILURE
    } else {
        ExitCode::SUCCESS
    }
}
