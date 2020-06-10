"""Make a random list of 1000 integers"""

import random

def make_lst():
    """Make a list of 1000 random integers"""
    lst = []
    for i in range(1000):
        lst.append(random.randint(0, 1000))

    return lst

lst = make_lst()

lst_hard_coded = [547, 107, 755, 212, 469, 614, 789, 436, 606, 733, 196, 950, 871, 283, 803, 304, 403, 430, 956, 219, 49, 215, 481, 996, 628, 642, 674, 419, 39, 923, 835, 523, 350, 522, 936, 191, 444, 916, 438, 234, 598, 427, 118, 544, 210, 84, 461, 410, 335, 488, 607, 67, 417, 350, 320, 486, 746, 327, 23, 731, 563, 538, 242, 954, 239, 38, 612, 289, 105, 57, 308, 894, 810, 800, 711, 414, 698, 676, 458, 694, 76, 740, 466, 416, 894, 636, 429, 731, 155, 591, 100, 862, 521, 774, 124, 344, 950, 199, 507, 428, 100, 404, 489, 529, 553, 958, 205, 987, 759, 356, 506, 261, 856, 734, 74, 889, 232, 526, 964, 377, 23, 207, 586, 191, 754, 155, 42, 731, 139, 847, 423, 965, 85, 304, 190, 994, 710, 391, 866, 245, 138, 637, 846, 461, 149, 761, 914, 655, 191, 882, 332, 746, 411, 145, 284, 725, 160, 862, 311, 579, 338, 193, 776, 370, 577, 215, 768, 202, 195, 92, 493, 944, 258, 864, 139, 861, 473, 811, 651, 805, 364, 878, 800, 481, 874, 313, 980, 858, 256, 893, 978, 273, 801, 5, 726, 556, 695, 113, 486, 78, 246, 68, 679, 753, 123, 62, 503, 312, 881, 784, 999, 157, 768, 309, 358, 383, 429, 971, 590, 925, 729, 376, 625, 774, 524, 191, 742, 389, 993, 229, 470, 44, 664, 93, 762, 455, 753, 837, 30, 427, 264, 845, 270, 270, 737, 589, 361, 956, 806, 822, 427, 217, 241, 175, 197, 390, 728, 985, 640, 233, 563, 421, 824, 294, 816, 333, 247, 552, 3, 617, 469, 110, 309, 674, 476, 628, 831, 165, 542, 998, 441, 560, 693, 651, 445, 439, 157, 199, 42, 500, 464, 988, 399, 928, 697, 385, 997, 707, 656, 392, 143, 875, 474, 823, 810, 761, 783, 850, 986, 63, 629, 521, 325, 933, 575, 230, 19, 354, 833, 433, 155, 258, 578, 259, 771, 803, 631, 516, 390, 866, 73, 241, 191, 340, 907, 84, 26, 656, 806, 44, 947, 341, 971, 142, 182, 183, 769, 590, 846, 524, 686, 688, 244, 897, 381, 266, 856, 671, 211, 721, 242, 887, 76, 468, 57, 808, 273, 98, 915, 631, 952, 744, 989, 535, 3, 416, 486, 486, 424, 415, 544, 948, 450, 137, 980, 479, 181, 101, 882, 238, 155, 916, 741, 626, 681, 183, 954, 817, 331, 42, 693, 225, 82, 344, 33, 96, 925, 568, 124, 1, 361, 779, 912, 600, 524, 744, 860, 35, 472, 697, 946, 903, 510, 302, 572, 614, 775, 13, 595, 503, 430, 174, 642, 95, 563, 513, 580, 510, 520, 975, 531, 426, 26, 950, 393, 120, 630, 555, 721, 955, 231, 577, 309, 117, 49, 961, 620, 744, 306, 7, 799, 989, 753, 771, 777, 858, 760, 123, 67, 55, 235, 835, 16, 183, 909, 506, 339, 505, 849, 233, 71, 73, 361, 102, 629, 803, 931, 796, 35, 390, 63, 681, 769, 292, 244, 608, 797, 123, 320, 809, 742, 866, 605, 868, 207, 481, 239, 221, 794, 614, 7, 117, 375, 473, 547, 122, 796, 967, 747, 412, 910, 957, 756, 501, 284, 477, 555, 954, 976, 350, 57, 261, 561, 965, 312, 792, 918, 35, 786, 490, 849, 224, 703, 270, 551, 518, 428, 707, 114, 201, 633, 627, 511, 204, 406, 769, 851, 80, 248, 400, 278, 674, 85, 809, 370, 56, 170, 694, 349, 761, 298, 579, 751, 322, 800, 792, 416, 800, 11, 111, 353, 86, 536, 386, 647, 597, 667, 258, 855, 856, 368, 393, 541, 601, 672, 692, 877, 76, 207, 843, 795, 567, 516, 847, 491, 253, 823, 51, 573, 346, 156, 274, 628, 922, 154, 872, 123, 359, 937, 410, 467, 310, 842, 100, 200, 216, 485, 192, 381, 479, 850, 493, 636, 700, 580, 452, 700, 490, 869, 877, 707, 923, 95, 234, 197, 587, 897, 728, 929, 324, 97, 31, 745, 905, 810, 135, 214, 444, 265, 16, 226, 97, 74, 600, 297, 253, 47, 251, 814, 762, 622, 820, 724, 504, 420, 840, 758, 901, 981, 857, 769, 294, 685, 166, 472, 320, 428, 824, 989, 326, 498, 923, 177, 674, 921, 529, 609, 953, 303, 771, 705, 434, 34, 580, 360, 723, 320, 810, 513, 609, 420, 944, 583, 91, 639, 792, 949, 376, 375, 235, 727, 54, 901, 280, 382, 365, 582, 750, 372, 335, 785, 612, 211, 456, 728, 448, 882, 766, 977, 428, 20, 582, 650, 15, 340, 909, 947, 587, 180, 329, 677, 398, 129, 951, 543, 609, 148, 79, 838, 614, 454, 135, 917, 259, 419, 459, 972, 121, 652, 685, 650, 427, 569, 77, 449, 200, 936, 518, 545, 376, 711, 935, 777, 231, 130, 910, 394, 295, 430, 550, 429, 549, 157, 279, 775, 581, 195, 6, 292, 451, 476, 271, 223, 354, 131, 302, 115, 961, 276, 76, 202, 480, 261, 458, 130, 399, 935, 28, 903, 582, 957, 788, 77, 498, 45, 893, 814, 253, 629, 179, 284, 429, 848, 996, 171, 67, 712, 516, 227, 982, 981, 511, 814, 612, 689, 971, 919, 533, 682, 211, 160, 465, 519, 335, 756, 113, 867, 13, 842, 80, 541, 968, 802, 483, 727, 230, 586, 208, 303, 333, 726, 594, 714, 216, 996, 768, 580, 980, 849, 464, 981, 57, 958, 986, 22, 804, 530, 320, 413, 42, 425, 270, 447, 333, 930, 547, 224, 475, 254, 654, 245, 161, 166, 206, 733, 81, 529, 596, 928, 697, 283, 441, 349, 480, 814, 55, 470, 773, 979, 197, 649, 764, 178, 548, 360, 355, 945, 74, 730, 80, 148, 828, 234, 835, 58, 791, 177, 419, 279, 253, 127, 666, 138, 40, 884, 754, 232, 55, 138, 541, 608, 1000, 298, 696, 50, 798, 881, 58, 266, 132, 482, 206, 947, 81, 603, 531, 223, 372, 329, 817, 812, 783, 950, 406, 678, 394, 409, 567, 800, 380, 940, 271, 289, 64, 892, 99, 290, 549, 651, 250, 581, 848, 52, 184, 149, 714, 382, 989, 827, 517]

