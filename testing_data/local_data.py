with open("/Users/areg.avetisyan/Desktop/data.txt", "r") as file1:
    whole_text_list = file1.readlines()

    HANDLE = whole_text_list[0][:-1]
    INVALID_HANDLE = whole_text_list[1][:-1]
    EXISTING_HANDLE = whole_text_list[2][:-1]
    EMAIL = whole_text_list[3][:-1]
    PASSWORD = whole_text_list[4][:-1]
    ERROR_MESSAGE_EXISTING = whole_text_list[5][:-1]
    ERROR_MESSAGE_INVALID = whole_text_list[6][:-1]
    INSTAGRAM = whole_text_list[7][:-1]
    TIKTOK = whole_text_list[8][:-1]
    YOUTUBE = whole_text_list[9][:-1]
    IMAGE_NAME = whole_text_list[10][:-1]
    IMAGE_PATH = whole_text_list[11][:-1]
    AVATAR_SHAPE = list(whole_text_list[12][:-1])
    NAME = whole_text_list[13][:-1]
    COUNTRY = whole_text_list[14][:-1]
    CATEGORIES = [whole_text_list[15][:-1], whole_text_list[16][:-1], whole_text_list[17][:-1],
                  whole_text_list[18][:-1], whole_text_list[19][:-1]]
    BIO = whole_text_list[20][:-1]
    CTA = whole_text_list[21]


TITLE = ("Insta Reel", "Insta Post", "Insta Story", "Tiktok Video", "YouTube Video", "Test")
CURRENCY = ("dollar", "euro", "pound", "", "", "")
RATES = (111, 2222.22, 99999.99, "", "", "")
