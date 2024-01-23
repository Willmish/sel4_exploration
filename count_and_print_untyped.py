#!/opt/homebrew/Caskroom/miniconda/base/bin/python3

# This scripts counts up all untypeds and actual sizes created during memory reuse and free mem initial allocation
# and the dump from seL4_BootInfo. It then prints the counts side by side for comparison.

text = """
SZYMS: Creating untypeds reuse mem region: start [ffffff8000100000..ffffff8000800000]
SZYMS: size ndks-boot freemem: 16
szymcounter: 0 Bit size: 28, reg start: [ffffff8000b37000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 12
szymcounter: 1 Bit size: 28, reg start: [ffffff8000b38000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 15
szymcounter: 2 Bit size: 28, reg start: [ffffff8000b40000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 18
szymcounter: 3 Bit size: 28, reg start: [ffffff8000b80000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 19
szymcounter: 4 Bit size: 28, reg start: [ffffff8000c00000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 22
szymcounter: 5 Bit size: 28, reg start: [ffffff8001000000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 24
szymcounter: 6 Bit size: 28, reg start: [ffffff8002000000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 25
szymcounter: 7 Bit size: 28, reg start: [ffffff8004000000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 26
szymcounter: 8 Bit size: 28, reg start: [ffffff8008000000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 27
szymcounter: 9 Bit size: 27, reg start: [ffffff8010000000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 27
szymcounter: 10 Bit size: 26, reg start: [ffffff8018000000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 26
szymcounter: 11 Bit size: 25, reg start: [ffffff801c000000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 25
szymcounter: 12 Bit size: 24, reg start: [ffffff801e000000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 24
szymcounter: 13 Bit size: 23, reg start: [ffffff801f000000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 23
szymcounter: 14 Bit size: 22, reg start: [ffffff801f800000..ffffff801fc00000]
MAx untyped bits size: 47
Actual size: 22
SZYMS: creation of untypeds for free memory region #0 at [ffffff8000b37000..ffffff801fc00000] success
szymcounter: 0 Bit size: 20, reg start: [ffffff801fe08800..ffffff801ffe0000]
MAx untyped bits size: 47
Actual size: 11
szymcounter: 1 Bit size: 20, reg start: [ffffff801fe09000..ffffff801ffe0000]
MAx untyped bits size: 47
Actual size: 12
szymcounter: 2 Bit size: 20, reg start: [ffffff801fe0a000..ffffff801ffe0000]
MAx untyped bits size: 47
Actual size: 13
szymcounter: 3 Bit size: 20, reg start: [ffffff801fe0c000..ffffff801ffe0000]
MAx untyped bits size: 47
Actual size: 14
szymcounter: 4 Bit size: 20, reg start: [ffffff801fe10000..ffffff801ffe0000]
MAx untyped bits size: 47
Actual size: 16
szymcounter: 5 Bit size: 20, reg start: [ffffff801fe20000..ffffff801ffe0000]
MAx untyped bits size: 47
Actual size: 17
szymcounter: 6 Bit size: 20, reg start: [ffffff801fe40000..ffffff801ffe0000]
MAx untyped bits size: 47
Actual size: 18
szymcounter: 7 Bit size: 20, reg start: [ffffff801fe80000..ffffff801ffe0000]
MAx untyped bits size: 47
Actual size: 19
szymcounter: 8 Bit size: 19, reg start: [ffffff801ff00000..ffffff801ffe0000]
MAx untyped bits size: 47
Actual size: 19
szymcounter: 9 Bit size: 18, reg start: [ffffff801ff80000..ffffff801ffe0000]
MAx untyped bits size: 47
Actual size: 18
szymcounter: 10 Bit size: 17, reg start: [ffffff801ffc0000..ffffff801ffe0000]
MAx untyped bits size: 47
Actual size: 17
SZYMS: creation of untypeds for free memory region #1 at [ffffff801fe08800..ffffff801ffe0000] success
SZYMS: creation of untypeds for free memory region #2 at [0..0] success
SZYMS: creation of untypeds for free memory region #3 at [0..0] success
SZYMS: creation of untypeds for free memory region #4 at [0..0] success
SZYMS: creation of untypeds for free memory region #5 at [0..0] success
SZYMS: creation of untypeds for free memory region #6 at [0..0] success
SZYMS: creation of untypeds for free memory region #7 at [0..0] success
SZYMS: creation of untypeds for free memory region #8 at [0..0] success
SZYMS: creation of untypeds for free memory region #9 at [0..0] success
SZYMS: creation of untypeds for free memory region #10 at [0..0] success
SZYMS: creation of untypeds for free memory region #11 at [0..0] success
SZYMS: creation of untypeds for free memory region #12 at [0..0] success
SZYMS: creation of untypeds for free memory region #13 at [0..0] success
SZYMS: creation of untypeds for free memory region #14 at [0..0] success
SZYMS: creation of untypeds for free memory region #15 at [0..0] success
Booting all finished, dropped to user space
    CSlot   	Paddr           	Size	Type
   0x138	               0	2^20	device untyped
   0x139	      0x1ffe0000	2^17	device untyped
   0x13a	      0x20000000	2^29	device untyped
   0x13b	      0x40000000	2^30	device untyped
   0x13c	      0x80000000	2^30	device untyped
   0x13d	      0xc0000000	2^29	device untyped
   0x13e	      0xe0000000	2^28	device untyped
   0x13f	      0xf0000000	2^27	device untyped
   0x140	      0xf8000000	2^26	device untyped
   0x141	      0xfc000000	2^25	device untyped
   0x142	      0xfe000000	2^23	device untyped
   0x143	      0xfe800000	2^22	device untyped
   0x144	      0xfec01000	2^12	device untyped
   0x145	      0xfec02000	2^13	device untyped
   0x146	      0xfec04000	2^14	device untyped
   0x147	      0xfec08000	2^15	device untyped
   0x148	      0xfec10000	2^16	device untyped
   0x149	      0xfec20000	2^17	device untyped
   0x14a	      0xfec40000	2^18	device untyped
   0x14b	      0xfec80000	2^19	device untyped
   0x14c	      0xfed00000	2^20	device untyped
   0x14d	      0xfee01000	2^12	device untyped
   0x14e	      0xfee02000	2^13	device untyped
   0x14f	      0xfee04000	2^14	device untyped
   0x150	      0xfee08000	2^15	device untyped
   0x151	      0xfee10000	2^16	device untyped
   0x152	      0xfee20000	2^17	device untyped
   0x153	      0xfee40000	2^18	device untyped
   0x154	      0xfee80000	2^19	device untyped
   0x155	      0xfef00000	2^20	device untyped
   0x156	      0xff000000	2^23	device untyped
   0x157	      0xff800000	2^22	device untyped
   0x158	      0xffc00000	2^21	device untyped
   0x159	      0xffe00000	2^20	device untyped
   0x15a	      0xfff00000	2^19	device untyped
   0x15b	      0xfff80000	2^18	device untyped
   0x15c	      0xfffc0000	2^17	device untyped
   0x15d	      0xfffe0000	2^16	device untyped
   0x15e	      0xffff0000	2^15	device untyped
   0x15f	      0xffff8000	2^14	device untyped
   0x160	      0xffffc000	2^13	device untyped
   0x161	      0xffffe000	2^12	device untyped
   0x162	      0xfffff000	2^11	device untyped
   0x163	      0xfffff800	2^10	device untyped
   0x164	      0xfffffc00	2^9	device untyped
   0x165	      0xfffffe00	2^8	device untyped
   0x166	      0xffffff00	2^7	device untyped
   0x167	      0xffffff80	2^6	device untyped
   0x168	      0xffffffc0	2^5	device untyped
   0x169	      0xffffffe0	2^4	device untyped
   0x16a	     0x100000000	2^32	device untyped
   0x16b	     0x200000000	2^33	device untyped
   0x16c	     0x400000000	2^34	device untyped
   0x16d	     0x800000000	2^35	device untyped
   0x16e	    0x1000000000	2^36	device untyped
   0x16f	    0x2000000000	2^37	device untyped
   0x170	    0x4000000000	2^38	device untyped
   0x171	    0x8000000000	2^46	device untyped
   0x172	  0x408000000000	2^45	device untyped
   0x173	  0x608000000000	2^44	device untyped
   0x174	  0x708000000000	2^43	device untyped
   0x175	  0x788000000000	2^42	device untyped
   0x176	  0x7c8000000000	2^41	device untyped
   0x177	  0x7e8000000000	2^40	device untyped
   0x178	  0x7f8000000000	2^39	device untyped
   0x179	        0x100000	2^20	untyped
   0x17a	        0x200000	2^21	untyped
   0x17b	        0x400000	2^22	untyped
   0x17c	        0xb37000	2^12	untyped
   0x17d	        0xb38000	2^15	untyped
   0x17e	        0xb40000	2^18	untyped
   0x17f	        0xb80000	2^19	untyped
   0x180	        0xc00000	2^22	untyped
   0x181	       0x1000000	2^24	untyped
   0x182	       0x2000000	2^25	untyped
   0x183	       0x4000000	2^26	untyped
   0x184	       0x8000000	2^27	untyped
   0x185	      0x10000000	2^27	untyped
   0x186	      0x18000000	2^26	untyped
   0x187	      0x1c000000	2^25	untyped
   0x188	      0x1e000000	2^24	untyped
   0x189	      0x1f000000	2^23	untyped
   0x18a	      0x1f800000	2^22	untyped
   0x18b	      0x1fe08800	2^11	untyped
   0x18c	      0x1fe09000	2^12	untyped
   0x18d	      0x1fe0a000	2^13	untyped
   0x18e	      0x1fe0c000	2^14	untyped
   0x18f	      0x1fe10000	2^16	untyped
   0x190	      0x1fe20000	2^17	untyped
   0x191	      0x1fe40000	2^18	untyped
   0x192	      0x1fe80000	2^19	untyped
   0x193	      0x1ff00000	2^19	untyped
   0x194	      0x1ff80000	2^18	untyped
   0x195	      0x1ffc0000	2^17	untyped
   """

import re

def count_bit_sizes_and_exponents(text):
    # Regular expression patterns
    actual_size_pattern = r"Actual size: (\d+)"
    untyped_size_pattern = r"\s2\^(\d+)\s+untyped"

    # Find all occurrences and convert to integers
    actual_sizes = [int(match) for match in re.findall(actual_size_pattern, text)]
    untyped_exponents = [int(match) for match in re.findall(untyped_size_pattern, text)]

    # Count occurrences
    actual_size_count = {size: actual_sizes.count(size) for size in set(actual_sizes)}
    untyped_exponent_count = {exp: untyped_exponents.count(exp) for exp in set(untyped_exponents)}

    return actual_size_count, untyped_exponent_count

def print_side_by_side(column1, column2):
    max_key = max(max(column1.keys(), default=0), max(column2.keys(), default=0))
    print(f"{'Actual Size Count':<20} | {'Untyped Exponent Count':<20}")
    print("-" * 43)

    for i in range(max_key + 1):
        col1_value = column1.get(i, '')
        col2_value = column2.get(i, '')
        print(f"{f'Size {i}: {col1_value}':<20} | {f'Exponent {i}: {col2_value}':<20}")


# Example usage
#text = """..."""  # replace with the input text
actual_size_count, untyped_exponent_count = count_bit_sizes_and_exponents(text)
print_side_by_side(actual_size_count, untyped_exponent_count)
