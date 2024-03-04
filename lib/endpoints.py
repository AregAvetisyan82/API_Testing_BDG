base = "https://api-mkit-dev.smclk.net"
login_user = base + "/api/auth/login"
reg_step1 = base + "/api/auth/register/check"
reg_step2 = base + "/api/auth/register/step2"
reg_step3 = base + "/api/auth/register/step3"
logout_user = base + "/api/auth/logout"
delete_user = base + "/api/profile/user"
me_info = base + "/api/auth/me"
list_info = base + "/api/mediakit-builder"
theme_colors = base + "/api/mediakit-builder/theme-colors"


def check_user_handle_availability(handle):
    return reg_step1 + f"?username={handle}"


def add_slug_for_mediakit_changes(upload_avatar=False, uplaod_image=False, uplaod_background=False):
    with open("/Users/areg.avetisyan/PycharmProjects/BDG/Beta_ViralMango/API_TESTING/testing_data/slug.txt", "r") \
            as file:
        slug = file.read()
    if upload_avatar:
        return list_info + f"/{slug}/upload-image"
    if uplaod_image:
        return list_info + f"/{slug}/upload-image/component"
    if uplaod_background:
        return list_info + f"/{slug}/upload-image/background"
    return list_info + f"/{slug}"


def get_countries(country=""):
    if country != "":
        return list_info + f"/countries?q={country}"
    return list_info + f"/countries"


def get_categories():
    return list_info + f"/categories"


def get_unsplash(search=False, image_name="", page=4, limit=30):
    if search:
        return list_info + f"/theme-unsplash-bg-images?q={image_name}&page={page}&limit={limit}"
    return list_info + f"/theme-unsplash-bg-images?page={page}&limit={limit}"


def get_components():
    return list_info + f"/components"
