
class user_module:

    def __init__(self) :
        self.usermap={}
        self.info=None
        self.username=None
    def sign_up(self,user_name,pswd):
        user=(user_name,pswd)
        self.username=user_name
        self.pswd=pswd
        self.usermap[user]={
            "color":"Black",
            "layout":"off",
            "notification":"off",
            "extreme_alert":"off",
            "background":""
        }

    def log_in(self,user_name,pswd):
        if (user_name,pswd) in self.usermap:
            self.info=self.usermap[(user_name,pswd)]
            self.username=user_name
            self.pswd=pswd
            return True
        else:
            return False
