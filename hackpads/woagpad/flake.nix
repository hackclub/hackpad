{
  description = "Cross compiling a rust program using rust-overlay";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

    flake-utils.url = "github:numtide/flake-utils";

    rust-overlay = {
      url = "github:oxalica/rust-overlay";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { nixpkgs, flake-utils, rust-overlay, ... }:
    flake-utils.lib.eachDefaultSystem (localSystem:
      let

        pkgs = import nixpkgs {
          inherit localSystem;
          overlays = [ (import rust-overlay) ];
        };

        toolchain = pkgs.rust-bin.stable.latest.default.override {
          extensions = ["rust-analyzer" "rust-src" "rustfmt" "llvm-tools"];
          targets = ["thumbv6m-none-eabi"];
        };
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [ toolchain pkgs.cargo-binstall pkgs.alejandra pkgs.flip-link pkgs.cargo-make pkgs.probe-rs pkgs.nixd pkgs.pkg-config pkgs.openssl ];
        };
      });
}
