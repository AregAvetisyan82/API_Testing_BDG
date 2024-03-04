class PayloadsAuthorization:
    def account_credentials(self, email="", password="", handle=""):
        user_request = {
            "email": f"{email}",
            "password": f"{password}",
            "username": f"{handle}"
        }
        return user_request


class PayloadsSocialPlatforms:
    def social_platform_accounts(self, instagram="", tiktok="", youtube=""):
        user_request = {
            "instagram": f"{instagram}",
            "tiktok": f"{tiktok}",
            "youtube": f"{youtube}"
        }
        return user_request


class PayloadsSystemProfile:
    def system_profile_credentials(self, avatar_shape="1", name="", country="", categories="", cta="Partner with me", bio=""):
        user_request = {
            "data[profile][avatar_shape]": f"{avatar_shape}",
            "data[profile][name][value]": f"{name}",
            "location": f"{country}",
            "categories": f"{categories}",
            "data[profile][cta]": f"{cta}",
            "bio": f"{bio}"
        }
        return user_request

    def fonts(self, group_id="", opt1_font="", opt2_font="", opt3_font=""):
        user_request = {
            "data[theme][fonts][group_id]": f"{group_id}",
            "data[theme][fonts][opt1][link]": f"{opt1_font}",
            "data[theme][fonts][opt2][link]": f"{opt2_font}",
            "data[theme][fonts][opt3][link]": f"{opt3_font}"
        }
        return user_request


class PayloadsBasicElements:
    def service_list_credentials(self, d_h=4, d_w=2, d_x=0, d_y=0, m_h=4, m_w=2, m_x=0, m_y=0, uid="",
                                 title=(), currency=(), rate=(), rates_number=1):
        service_list = [
            {"currency": currency[0], "title": title[0], "rate": rate[0]},
            {"currency": currency[1], "title": title[1], "rate": rate[1]},
            {"currency": currency[2], "title": title[2], "rate": rate[2]},
            {"currency": currency[3], "title": title[3], "rate": rate[3]},
            {"currency": currency[4], "title": title[4], "rate": rate[4]},
            {"currency": currency[5], "title": title[5], "rate": rate[5]}
        ]
        user_request = {
            "data": {
                "components": [{
                    "name": "service_list",
                    "uid": uid,
                    "desktop": {"h": d_h, "w": d_w, "x": d_x, "y": d_y},
                    "mobile": {"h": m_h, "w": m_w, "x": m_x, "y": m_y},
                    "service_list": service_list[0:rates_number]
                }]
            }
        }
        return user_request

    def image_credentials(self, d_h=4, d_w=2, d_x=0, d_y=0, m_h=4, m_w=2, m_x=0, m_y=0, image_url=""):
        user_request = {
            "data": {
                "components": [{
                        "name": "image",
                        "desktop": {"h": d_h, "w": d_w, "x": d_x, "y": d_y},
                        "mobile": {"h": m_h, "w": m_w, "x": m_x, "y": m_y},
                        "image_url": f"{image_url}"}]}
        }
        return user_request


class ImageUpload:
    def upload_image(self, file_name="", file_path=""):
        file = [('image', (f'{file_name}', open(f'{file_path}', 'rb'), 'image/jpeg'))]
        return file

    def background_image(self, bg_image=""):
        user_request = {
            "data[theme][bg_image]": bg_image
        }
        return user_request
