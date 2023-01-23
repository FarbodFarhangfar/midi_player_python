from .config import NoteDic, TimeValues


class Parse:
    def __init__(self):
        pass

    def get_notes(self, note_str):
        note_list = note_str.split()
        note_dict = NoteDic()
        note_dic = note_dict.get_note_dic()
        r_note_list = []
        for notes in note_list:
            if notes[-1].isdigit():
                if notes[:-1] not in note_dic:
                    raise Exception("wrong note name")
                else:
                    r_note_list.append(notes)
            else:
                if notes not in note_dic:
                    raise Exception("wrong note name")
                else:
                    r_note_list.append(notes + "5")

        return r_note_list

    def get_dur(self, dur_str):
        dur_list = dur_str.split()
        dur_dic = TimeValues()
        dur_dic = dur_dic.get_value_list()
        r_dur_list = []
        for notes in dur_list:
            if notes not in dur_dic:
                raise Exception("wrong note value")
            else:
                r_dur_list.append(dur_dic[notes])

        return r_dur_list



