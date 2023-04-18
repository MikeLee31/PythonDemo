class Videos(object):

    def __init__(self, v_id, a_id, v_code, name, a_name, date, img_url):
        self.v_id = v_id
        self.a_id = a_id
        self.v_code = v_code
        self.name = name
        self.a_name = a_name
        self.date = date
        self.img_url = img_url

    def __str__(self):
        return f'{self.v_code}-{self.name}-{self.a_name}'


if __name__ == '__main__':
    v = Videos(1, 2, 'SS', "Vname", 'Aname', '2021=2', 'sdafdas')
    print(v.__str__())

