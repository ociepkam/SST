#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import gui
import yaml

__author__ = 'ociepkam'

CONFIG_KEYS = [
    # Observer info
    'Observer',
    # Experiment length
    'Number_of_training_trials', 'Number_of_experiment_blocks', 'Number_of_experiment_trials',
    # Trial info
    'Arrow_show_time', 'Percent_of_trials_with_stop', 'Start_wait_to_stop', 'Stop_show_time', 'Resp_time',
    'Rest_time', 'Rest_time_jitter',
    # Triggers info
    'Ophthalmic_procedure', 'Send_EEG_trigg', 'Send_Nirs_trigg',
    # View info
    'Text_size', 'Fix_time', 'Break_between_fix_and_arrow', 'Screen_color'
]


def main():
    my_dlg = gui.Dlg(title="SST - config")
    my_dlg.addText('Observer info')
    my_dlg.addField('Observer')

    my_dlg.addText('Experiment length')
    my_dlg.addField('Number_of_training_trials', 4)
    my_dlg.addField('Number_of_experiment_blocks', 1)
    my_dlg.addField('Number_of_experiment_trials', 4)

    my_dlg.addText('Trial info')
    my_dlg.addField('Arrow_show_time', 1)
    my_dlg.addField('Percent_of_trials_with_stop', 25)
    my_dlg.addField('Start_wait_to_stop', 1)
    my_dlg.addField('Stop_show_time', 1)
    my_dlg.addField('Resp_time', 2)
    my_dlg.addField('Rest_time', 1)
    my_dlg.addField('Rest_time_jitter', 1)

    my_dlg.addText('Triggers info')
    my_dlg.addField('Ophthalmic_procedure', choices=['False', 'True'])
    my_dlg.addField('Send_EEG_trigg', choices=['False', 'True'])
    my_dlg.addField('Send_Nirs_trigg', choices=['False', 'True'])

    my_dlg.addText('View info')
    my_dlg.addField('Text_size', 1)
    my_dlg.addField('Fix_time', 1)
    my_dlg.addField('Break_between_fix_and_arrow', 1)
    my_dlg.addField('Screen_color', 1)

    my_dlg.show()
    if not my_dlg.OK:
        exit(1)

    if len(CONFIG_KEYS) != len(my_dlg.data):
        raise Exception("Problems with config")

    args_dict = dict()
    for idx, key in enumerate(CONFIG_KEYS):
        if isinstance(my_dlg.data[idx], unicode):
            my_dlg.data[idx] = str(my_dlg.data[idx])
        if my_dlg.data[idx] == 'False':
            my_dlg.data[idx] = False
        elif my_dlg.data[idx] == 'True':
            my_dlg.data[idx] = True
        args_dict[key] = my_dlg.data[idx]

    args_dict['Keys'] = ['lctrl', 'rctrl']
    args_dict['Possible_wait_to_stop'] = [args_dict['Start_wait_to_stop']]

    with open("docs/config.yaml", 'w') as save_file:
        save_file.write(yaml.dump(args_dict))


if __name__ == '__main__':
    main()
