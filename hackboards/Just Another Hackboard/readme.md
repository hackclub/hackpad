**Just Another Hackboard**

It's what the title says, just another hackboard.
But seriously, this is a 75% keyboard which I designed over the course of a couple of days for fun and to see just how hard designing a keyboard could be!

Spoilers: It was difficult.

Schematic:
![image](https://github.com/user-attachments/assets/e7a38927-3d77-436f-b328-701bc1124f09)
![image](https://github.com/user-attachments/assets/6f2aa29f-deaf-46ef-ac56-3ba0a11f4d1b)
![image](https://github.com/user-attachments/assets/6607ca3a-f9d2-424d-bef2-c37913acca1f)

Arguably the easiest part of the project, the schematic was more just tedious in the sense that wiring the LED matrix along with the switches got pretty tiring after the first 5 or so minutes.
However, it didn't take me too long to make the whole schematic, people on slack helped me with choosing the correct MRC to wire it all to.

PCB:

![image](https://github.com/user-attachments/assets/79c1f397-91e0-4369-9c15-ad88463334f2)

Ever felt like wiring 700 wires on a pcb? Well now you can!
The pcb design was probably my favourite part and took me more than a few hours over a few days to get all the wiring done to a point where I was happy with it.
The initial positioning also took a while because I was pulling my hair out trying to calculate the sizes of different keycaps (e.g. Tab and caps lock) so the keycaps didn't overlap.
That *was* until I was helping someone on slack and saw they had different sized outlines for the keycaps and decided to take a second look at the footprint library... and lo and behold, people aren't masochists and made different sized footprints for the different keys...
Good news - I got all the measurements right on my own :D.
Bad news - I wasted about an hour doing that :(.

Case:

Fully Assembled:

![image](https://github.com/user-attachments/assets/4ea43f57-9278-49d4-b2c0-d80f60a2ee00)

![image](https://github.com/user-attachments/assets/c912326d-1a4c-4c4a-937b-f37688a0bf6c)

(Note: MRC pins are clipping through the case in the second screenshot, this shouldn't be an issue when building the keyboard to the best of my knowledge)

Top Case:

![image](https://github.com/user-attachments/assets/c15ccecc-b048-4b0d-b3d6-72bb347be2b7)

![image](https://github.com/user-attachments/assets/7147ca92-0de1-4036-9acf-cbc7e33c0398)

Bottom Case:

![image](https://github.com/user-attachments/assets/411e294e-dc8e-4765-ad6c-d305704a2e55)

![image](https://github.com/user-attachments/assets/40052b47-057d-46b4-a31c-3b82b084adfb)

This is the part I changed after my initial PR since there was an issue with the switch holes not aligning properly with the switches themselves along with there not being holes for the stabilsers and 2 screws. This in itself took a while seeing as I initially eyeballed the measurements for the stabilisers before being told to just go to ai03's plate generator (which I should've done from the start). That turned out to be much quicker than scouring the internet for the dimensions thankfully).
After fixing those issues, I saw a nice design from aryatajne28's reaperboard and decided to make one of my own - initially making a separate top and middle plate but merging them in the end in order to fix an issue where screwing the case together wouldn't actually attach the case layers.
I also changed how the art for my board is done - I liked the idea of seeing the MRC through the case but thought that a grate would look weird on the board. The top of my case also looked barren at the top due to it having a "massive forehead" (thanks ben) so I also had to find a solution for that. Luckily, I thought of the idea of using the top of the PCB (also barren) as the art, putting a lot of silkscreen art there to make it look nicer! This not only solved the art problem, but also lets me see the MRC (yay!).
The art includes boywithuke, chiikawa, orpheus and some handpicked quotes from my friends. I've put a gap in the top plate so I can put an acrylic plate there when I order my parts.
The feet of the case were ***heavily inspired*** (carbon copied) from my current keyboard (Logitech G513) since imo they're pretty perfect and I like them. Plus my hands are already used to the angle of my current keyboard so copying the feet in theory should make this keyboard also feel nice!
I've modelled the parts for the feet and stabilising holes separately and can ask a friend to print them for me instead of asking for them from HQ - if I need to add the files anyway just lmk!

Firmware:

There's not much to put here since I've learned a lot from the hackpad firmware incident, meaning this part only took like 30 minutes to do :D.
It's basic firmware (led controls, matrix and rotary encoder controls) which I plan on expanding and developing when I have the board to experiment with since it'll be easier to do then.

BOM:

| Item | Quantity | Price | Notes |
| Orpheus Pico | 1 | N/A (from HQ) | None |
| PCB | 5 (min) | $40.35 | None |
| [Gateron Red Switches](https://www.aliexpress.com/item/1005005550328893.html?spm=a2g0o.productlist.main.8.2f7f7150eWzJNT&aem_p4p_detail=202506080953021465465888897560003911256&algo_pvid=33e5ce8c-8cb6-4f81-86de-9046f2a9f0ac&algo_exp_id=33e5ce8c-8cb6-4f81-86de-9046f2a9f0ac-7&pdp_ext_f=%7B%22order%22%3A%22662%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21GBP%214.61%213.62%21%21%216.07%214.77%21%402103835e17494015820245584eae94%2112000033504668219%21sea%21UK%210%21ABX&curPageLogUid=MwMlj8fFEqvK&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=202506080953021465465888897560003911256_2) | 90 | $22.43 | None |
| [EC11 Rotary Encoder](https://www.aliexpress.com/item/4000911785652.html?spm=a2g0o.productlist.main.5.62b32671VAKecz&algo_pvid=9e0890ab-3a0f-4ae8-9276-73388fd81955&algo_exp_id=9e0890ab-3a0f-4ae8-9276-73388fd81955-2&pdp_ext_f=%7B%22order%22%3A%2247%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21GBP%210.90%210.78%21%21%211.13%210.98%21%40211b618e17424131559716674e1e90%2110000010539216633%21sea%21UK%210%21ABX&curPageLogUid=ffkDZnXSsCcj&utparam-url=scene%3Asearch%7Cquery_from%3A) | 1 | $1.39 | None |
| [SK6812 MINIE LEDs](https://www.aliexpress.com/item/1005004249903121.html?spm=a2g0o.productlist.main.37.7af85pmJ5pmJqk&algo_pvid=8c7a5ea7-f458-4e97-aaa2-8f9b79d97329&algo_exp_id=8c7a5ea7-f458-4e97-aaa2-8f9b79d97329-18&pdp_ext_f=%7B%22order%22%3A%2234%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21GBP%2115.33%2110.96%21%21%2119.27%2113.78%21%40211b613917421674405453531e93e5%2112000028520276327%21sea%21UK%210%21ABX&curPageLogUid=JZ6IYBnz0uC4&utparam-url=scene%3Asearch%7Cquery_from%3A) | 100 | $14.11 | None |
| [1N4148 Diodes](https://www.aliexpress.com/item/4000142272546.html?spm=a2g0o.productlist.main.2.735067ddyTMuJc&algo_pvid=fec3629a-acaf-4354-9f12-13d795d84c55&algo_exp_id=fec3629a-acaf-4354-9f12-13d795d84c55-1&pdp_ext_f=%7B%22order%22%3A%221815%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21GBP%211.19%210.81%21%21%2111.30%217.70%21%40210385bb17494021031734897ea6e9%2110000000428321629%21sea%21UK%210%21ABX&curPageLogUid=RL3OxzDUpyMF&utparam-url=scene%3Asearch%7Cquery_from%3A) | 100 | $1.10 | None |
| [PBT Side Printed Keycaps](https://www.amazon.co.uk/PBT-Keycaps-Minimalist-Mechanical-Keyboards/dp/B0BZCFFB94/ref=sr_1_4?crid=3CJVCWWTIXSZC&dib=eyJ2IjoiMSJ9.-mHMjP_BmZ25B8LQu0m3dCQhHV4M95rb1lZQ7p6S3F-HPC5wnUEMVESuynOHin3OVQT9qNhwNlVOEw9dzIA9VrCvIDXsWnjMDsZBFPla0Dlga5Kn31kxg0ChNFtf11zjBKriaMgnkxk98en5kk4FcAVK0aMJDV1rmgmRYcEjWi9VrF6q4Paf_ZouNvqXsFDzoSC7Zp931EBfCTud8alwKIvVihh7J2LKqt0hn5EomHk.cmPxU1z0y1_UQiCK2pBZgwjAaG2T4qeUbMdxiPmK7Bs&dib_tag=se&keywords=iso%2Bkeycaps%2B75%25&qid=1742170636&sprefix=iso%2Bkeycaps%2B75%25%2Caps%2C61&sr=8-4&th=1) | 1 | $22.23 | None |
| [Aluminium Alloy Knob](https://www.aliexpress.com/item/1005008054145777.html?spm=a2g0o.productlist.main.3.3298pF0GpF0GKG&algo_pvid=dd0c1415-7c6c-4f84-ab6c-3cfc36ac088d&algo_exp_id=dd0c1415-7c6c-4f84-ab6c-3cfc36ac088d-2&pdp_ext_f=%7B%22order%22%3A%2257%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21GBP%213.36%212.75%21%21%214.43%213.63%21%40210388c917494023116053534ef736%2112000043462088003%21sea%21UK%210%21ABX&curPageLogUid=gai0n1VfPVXH&utparam-url=scene%3Asearch%7Cquery_from%3A) | 2 | $3.72 | Can 3D print if necessary |
| [Sarini Stabilisers 2U etc.](https://www.amazon.co.uk/Sarini-Stabilizers-Stabilizer-Replacement-Accessories/dp/B0D6VF4SQB/ref=sr_1_4?crid=2KCKFSMH49UTE&dib=eyJ2IjoiMSJ9.Y7bI0HCJ5jJu9W8mk2Oc1jZz8aztxGKzlwEJmlLEbcRRkfR2VJwT15xxfYmwPCxdecmvbbx0UCYbv0bYzhmw6_KEjYpbUicMTkmWZ1qLPceNrKuxlnGPSgWjK1o6_mTKLA9uMO5w3p0bU2btaNV6d-m2vIa96hq-Rni3JlgGRGFo_7mpruQ6XpebJdEU2NYDZ4J7557-R2a2XTXv44W93TsBCPXOYgEYkYBHqoPf14w.TrMGy3DaCrDZfB0lNJzvSSh8TvosaJTck1p1SynDWvM&dib_tag=se&keywords=keyboard+stabilisers&qid=1742170441&s=instant-video&sprefix=keyboard+stabilisers%2Cinstant-video%2C63&sr=1-4) | 7 | $13.52 | None |
| [3x16mm Steel Screws](https://www.amazon.co.uk/16mm-Small-Steel-Countersunk-Screws/dp/B083M983XD/ref=sr_1_1?crid=2YCIW8N84CPBZ&dib=eyJ2IjoiMSJ9.sxY40KHto88NbNTRrNYqFNL_xAMeXLNzbxHxQnpeCfi-GY3AuMJ3yvpAIIYh_KnruBCnlyq_gDdp6uj0aEKvaA-7iQr3zwnGwd5Fk3rww1SoOPqroQInLNOEuiwm7JWGc2ndfOiMKpbjvQqAovhuFJ5Pg_adaYuQfy6zO36taAhByr5hqUsc2U4WogbjRkfpIwopi3Ss-tReO-OjxC_CeQ5LFdwkFd0GdVhTrONCpo4.mlhAqYAFh7roaa1RBOHHbjo9X3jp3TkcGUi6Nq6y4FE&dib_tag=se&keywords=3x16mm+screws+and+inserts&qid=1742393021&s=instant-video&sprefix=3x16mm+screws+and+insets%2Cinstant-video%2C53&sr=1-1) | 100 | $5.40 | None |
| [Threaded Brass Heatset Inserts](https://www.amazon.co.uk/Threaded-Inserts-Printing-Knurled-Automotive/dp/B0BVMK6DTK/ref=sr_1_20?crid=304TAPBP0T1RK&dib=eyJ2IjoiMSJ9.SLzAz5nvMLiSfDW9QBVN_cugMbC4GfU3uKWASzXesm-kiWVugTADAXMm_qTBywAInMS5mNBqbdhyPqE32-XXjMZdG2OqQ7MFTtAwnNpw62FpYwHZE1b6Ysuybw49Uo1TiUVirAqYjy5nNVM_pOQHHJDuektypkxMjbRKS_JpbWzctG5IuTbPZc6AjH-h53x9YzoVGigfiKn1GAVVgnw4twayiqmo7o2OlLdHWkeCzkI8QPy6Gq4CeIAQIBp5yCc1pi-IdIaU8EjI4T0pg7XRcE1vCO1ZgYUXOY4xtkNhsV2ZlgEmutTbXIKZ3i1ue99AFU5CLtm8Q37hBSWaoHwP0lGsa7_VPlfe2HjoHr5fhJIWTErSWuIj7hTF20UiWwM3EZ1-D5gWIxIi-GfIkPFCU7qNFMhCroWv16tnf3efMuCNoFZDB__EW9xNmfw3jIqq.mb_GctK0GSdkZogRRybOBcjlYJpu2nEPvJNbHE7pmtQ&dib_tag=se&keywords=M3x16mm+heat+inserts&qid=1742397968&sprefix=m3x16mm+heat+inserts%2Caps%2C53&sr=8-20) | 100 | $7.29 | None |
| Acrylic Sheet (1mm thickness) | 1 | $5.34 | Can buy myself if this doesn't fit into the grant |
