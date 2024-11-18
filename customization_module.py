import user_module

class customization_module:
    def __init__(self,user):
        self.user=user

    def set_color(self,color):
        self.user.usermap[(self.user.username,self.user.pswd)]["color"]=color

    def get_color(self):
        if self.user.username!=None:
            return self.user.usermap[(self.user.username,self.user.pswd)]["color"]
        else: return "Black"
    def set_layout(self,layout):
        self.user.usermap[(self.user.username,self.user.pswd)]["layout"]=layout

    def get_layout(self):
        return self.user.usermap[(self.user.username,self.user.pswd)]["layout"]
    
    def set_notification(self,notification):
        self.user.usermap[(self.user.username,self.user.pswd)]["notification"]=notification
    
    def get_notification(self):
        return self.user.usermap[(self.user.username,self.user.pswd)]["notification"]

    def set_extreme_alert(self,extreme_alert):
        self.user.usermap[(self.user.username,self.user.pswd)]["extreme_alert"]=extreme_alert

    def get_extreme_alert(self):
        return self.user.usermap[(self.user.username,self.user.pswd)]["extreme_alert"]

    def set_background(self,background):
        self.user.usermap[(self.user.username,self.user.pswd)]["background"]=background

    def get_background(self):
        return self.user.usermap[(self.user.username,self.user.pswd)]["background"]