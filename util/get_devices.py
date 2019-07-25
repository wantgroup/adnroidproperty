from dos_cmd import DosCmd
class Server:
    def __init__(self):
        #执行控制台的命令使用
        self.dos = DosCmd()
        #获取设备devices的集合
        self.device_list = self.get_devices()
        
    def get_devices(self):
        '''
        获取设备devices的集合
        '''
        devices_list = []
        #执行adb devices命令来获取 devices list
        result_list = self.dos.excute_cmd_result('adb devices')
        #取出devicees存入devices_list中
        if len(result_list)>=2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

if __name__ == '__main__':
   s=Server().get_devices()
   print(s)