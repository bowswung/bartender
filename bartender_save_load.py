from config import SAVE_FILENAME
from interface_bar import InterfaceBar
from interface_info_panel import InterfaceInfoPanel

def save(bartender):
    if bartender.overlay is None:
        print("<Save> The game was not runing! I am not saving the settings!")
        return

    with open(SAVE_FILENAME, 'w') as f: 
        w = lambda x: f.write(str(x) +"\n")
        # Saving data - completed researches
        w(bartender.w_checkbox_completed_researches.checkState())
        w(bartender.w_checkbox_completed_researches_times.checkState())
        w(bartender.overlay.research_list.cols)
        w(bartender.overlay.research_list.rows)
        w(bartender.overlay.research_list.x())
        w(bartender.overlay.research_list.y())
        w(bartender.overlay.research_list.expand_index)

        # Researching bars
        w(bartender.w_checkbox_researches.checkState())
        w(bartender.w_checkbox_researches_show_bars.checkState())
        w(bartender.overlay.research_bars.cols)
        w(bartender.overlay.research_bars.rows)
        w(bartender.overlay.research_bars.x())
        w(bartender.overlay.research_bars.y())
        w(bartender.overlay.research_bars.expand_index)

        # Offscreen units
        widget = bartender.w_tabs_settings.widget(0)
        w(widget.w_text_name.text())
        w(widget.w_checkbox_hidden.checkState())
        w(widget.w_checkbox_selected.checkState())
        w(widget.w_checkbox_selected_policy.checkState())
        w(widget.w_text_selected_min.value())
        w(widget.w_text_selected_max.value())
        w(widget.w_checkbox_monks_relic.checkState())
        w(widget.w_checkbox_monks_relic_policy.checkState())
        w(widget.w_text_monks_relic_min.value())
        w(widget.w_text_monks_relic_max.value())
        w(widget.w_checkbox_group1.checkState())
        w(widget.w_checkbox_group1_policy.checkState())
        w(widget.w_text_group1_min.value())
        w(widget.w_text_group1_max.value())
        w(widget.w_checkbox_group2.checkState())
        w(widget.w_checkbox_group2_policy.checkState())
        w(widget.w_text_group2_min.value())
        w(widget.w_text_group2_max.value())
        w(widget.w_checkbox_group3.checkState())
        w(widget.w_checkbox_group3_policy.checkState())
        w(widget.w_text_group3_min.value())
        w(widget.w_text_group3_max.value())
        w(widget.w_checkbox_group4.checkState())
        w(widget.w_checkbox_group4_policy.checkState())
        w(widget.w_text_group4_min.value())
        w(widget.w_text_group4_max.value())
        w(widget.w_checkbox_group5.checkState())
        w(widget.w_checkbox_group5_policy.checkState())
        w(widget.w_text_group5_min.value())
        w(widget.w_text_group5_max.value())
        w(widget.w_checkbox_group6.checkState())
        w(widget.w_checkbox_group6_policy.checkState())
        w(widget.w_text_group6_min.value())
        w(widget.w_text_group6_max.value())
        w(widget.w_checkbox_group7.checkState())
        w(widget.w_checkbox_group7_policy.checkState())
        w(widget.w_text_group7_min.value())
        w(widget.w_text_group7_max.value())
        w(widget.w_checkbox_group8.checkState())
        w(widget.w_checkbox_group8_policy.checkState())
        w(widget.w_text_group8_min.value())
        w(widget.w_text_group8_max.value())
        w(widget.w_checkbox_group9.checkState())
        w(widget.w_checkbox_group9_policy.checkState())
        w(widget.w_text_group9_min.value())
        w(widget.w_text_group9_max.value())
        w(widget.w_checkbox_group0.checkState())
        w(widget.w_checkbox_group0_policy.checkState())
        w(widget.w_text_group0_min.value())
        w(widget.w_text_group0_max.value())
        w(widget.w_checkbox_civilians.checkState())
        w(widget.w_checkbox_civilians_policy.checkState())
        w(widget.w_text_civilians_min.value())
        w(widget.w_text_civilians_max.value())
        w(widget.w_checkbox_military.checkState())
        w(widget.w_checkbox_military_policy.checkState())
        w(widget.w_text_military_min.value())
        w(widget.w_text_military_max.value())


        for i in range(1, bartender.w_tabs_settings.count()):
            widget = bartender.w_tabs_settings.widget(i)
            if type(widget) == InterfaceBar:
                w("InterfaceBar")
                w(widget.w_text_name.text())
                w(widget.w_checkbox_aggregate.checkState())
                w(widget.w_checkbox_hidden.checkState())
                w(widget.w_text_idle_time_for_pulsing.value())
                w(widget.w_text_idle_time_for_blinkin.value())
                w(widget.w_combo_timer_number.currentIndex())
                w(widget.w_combo_top_number.currentIndex())
                w(widget.w_combo_top_number_aggr.currentIndex())
                w(widget.w_combo_bottom_number.currentIndex())
                w(widget.w_combo_bottom_number_aggr.currentIndex())
                w(widget.w_checkbox_show_all_units.checkState())
                w(widget.w_checkbox_show_civilians.checkState())
                w(widget.w_checkbox_show_military.checkState())
                w(widget.w_checkbox_show_trade_units.checkState())
                w(widget.w_checkbox_show_fish_ships.checkState())
                w(widget.w_checkbox_show_villagers.checkState())
                w(widget.w_checkbox_show_food_vills.checkState())
                w(widget.w_checkbox_show_wood_vills.checkState())
                w(widget.w_checkbox_show_gold_vills.checkState())
                w(widget.w_checkbox_show_stone_vills.checkState())
                w(widget.w_checkbox_show_swordsmen.checkState())
                w(widget.w_checkbox_show_pikemen.checkState())
                w(widget.w_checkbox_show_eagles.checkState())
                w(widget.w_checkbox_show_huskarls.checkState())
                w(widget.w_checkbox_show_condottieros.checkState())
                w(widget.w_checkbox_show_light_cavalry.checkState())
                w(widget.w_checkbox_show_heavy_cavalry.checkState())
                w(widget.w_checkbox_show_camels.checkState())
                w(widget.w_checkbox_show_tarkans.checkState())
                w(widget.w_checkbox_show_battle_elephants.checkState())
                w(widget.w_checkbox_show_archers.checkState())
                w(widget.w_checkbox_show_skirmishers.checkState())
                w(widget.w_checkbox_show_cavalry_archers.checkState())
                w(widget.w_checkbox_show_genitours.checkState())
                w(widget.w_checkbox_show_hand_cannoneers.checkState())
                w(widget.w_checkbox_show_siege_rams.checkState())
                w(widget.w_checkbox_show_onagers.checkState())
                w(widget.w_checkbox_show_scorpions.checkState())
                w(widget.w_checkbox_show_bombard_cannons.checkState())
                w(widget.w_checkbox_show_siege_towers.checkState())
                w(widget.w_checkbox_show_war_ships.checkState())
                w(widget.w_checkbox_show_fire_ships.checkState())
                w(widget.w_checkbox_show_demolition_ships.checkState())
                w(widget.w_checkbox_show_cannon_galleons.checkState())
                w(widget.w_checkbox_show_unique_unit_ships.checkState())
                w(widget.w_checkbox_show_petards.checkState())
                w(widget.w_checkbox_show_trebuchets.checkState())
                w(widget.w_checkbox_show_unique_units.checkState())
                w(widget.w_checkbox_show_monks.checkState())
                w(widget.w_checkbox_show_transport_ships.checkState())
                w(widget.w_checkbox_show_all_buildings.checkState())
                w(widget.w_checkbox_show_town_centers.checkState())
                w(widget.w_checkbox_show_lumber_camps.checkState())
                w(widget.w_checkbox_show_mining_camps.checkState())
                w(widget.w_checkbox_show_mills.checkState())
                w(widget.w_checkbox_show_barracks.checkState())
                w(widget.w_checkbox_show_archery_ranges.checkState())
                w(widget.w_checkbox_show_stables.checkState())
                w(widget.w_checkbox_show_siege_workshops.checkState())
                w(widget.w_checkbox_show_monastries.checkState())
                w(widget.w_checkbox_show_castles.checkState())
                w(widget.w_checkbox_show_docks.checkState())
                w(widget.w_checkbox_show_blacksmiths.checkState())
                w(widget.w_checkbox_show_universities.checkState())
                w(widget.w_checkbox_show_markets.checkState())
                w(widget.w_checkbox_show_towers.checkState())
                w(widget.w_checkbox_show_slingers.checkState())
                w(widget.w_checkbox_show_livestock.checkState())
                w(widget.w_checkbox_show_gates.checkState())
                w(widget.w_checkbox_show_walls.checkState())
                w(widget.w_text_hp_min.value())
                w(widget.w_text_hp_max.value())
                w(widget.w_text_idle_min.value())
                w(widget.w_text_idle_max.value())
                w(widget.w_filter_training.checkState())
                w(widget.w_filter_researching.checkState())
                w(widget.w_filter_constucted.checkState())
                w(widget.w_filter_selected.checkState())
                w(widget.w_filter_group0.checkState())
                w(widget.w_filter_group1.checkState())
                w(widget.w_filter_group2.checkState())
                w(widget.w_filter_group3.checkState())
                w(widget.w_filter_group4.checkState())
                w(widget.w_filter_group5.checkState())
                w(widget.w_filter_group6.checkState())
                w(widget.w_filter_group7.checkState())
                w(widget.w_filter_group8.checkState())
                w(widget.w_filter_group9.checkState())
                w(widget.icon_list.cols)
                w(widget.icon_list.rows)
                w(widget.icon_list.x())
                w(widget.icon_list.y())
                w(widget.icon_list.expand_index)
            elif type(widget) == InterfaceInfoPanel:
                w("InterfaceInfoPanel")
                w(widget.w_text_name.text())
                w(widget.w_checkbox_hidden.checkState())
                w(widget.w_checkbox_wood.checkState())
                w(widget.w_checkbox_food.checkState())
                w(widget.w_checkbox_gold.checkState())
                w(widget.w_checkbox_stone.checkState())
                w(widget.w_checkbox_fish.checkState())
                w(widget.w_checkbox_trade.checkState())
                w(widget.w_checkbox_resources.checkState())
                w(widget.w_checkbox_resources_carrying.checkState())
                w(widget.w_checkbox_idle_vills.checkState())
                w(widget.w_checkbox_idle_vills_time.checkState())
                w(widget.w_checkbox_farm_reseeds.checkState())
                w(widget.w_checkbox_relics.checkState())
                w(widget.w_checkbox_civilians.checkState())
                w(widget.w_checkbox_military.checkState())
                w(widget.w_checkbox_kd_units.checkState())
                w(widget.w_checkbox_kd_buildings.checkState())
                w(widget.w_checkbox_game_time.checkState())
                w(widget.overlay_panel.x())
                w(widget.overlay_panel.y())
                w(widget.overlay_panel.width())
                w(widget.overlay_panel.height())
                w(widget.overlay_panel.expand_index)
                



global stuff

def load_geometry(bartender):        
    global stuff
    cols, rows, x, y, expand_index = stuff[0]
    bartender.overlay.research_list.set_geomatry_by_grid(cols, rows)
    bartender.overlay.research_list.setGeometry(x, y, bartender.overlay.research_list.width(), bartender.overlay.research_list.height())
    bartender.overlay.research_list.set_expand_index(expand_index)

    cols, rows, x, y, expand_index = stuff[1]
    bartender.overlay.research_bars.set_geomatry_by_grid(cols, rows)
    bartender.overlay.research_bars.setGeometry(x, y, bartender.overlay.research_bars.width(), bartender.overlay.research_bars.height())
    bartender.overlay.research_bars.set_expand_index(expand_index)

    for idx in range(1, bartender.w_tabs_settings.count()):
        widget = bartender.w_tabs_settings.widget(idx)
        cols, rows, x, y, expand_index = stuff[1+idx] # stuff[0] stuff[1] is used; loop starting with 1 => first iteration has index 2 thus stuff[2]
        if type(widget) == InterfaceBar:
            widget.icon_list.set_geomatry_by_grid(cols, rows)
            widget.icon_list.setGeometry(x, y, widget.icon_list.width(), widget.icon_list.height())
            widget.icon_list.set_expand_index(expand_index)
        elif type(widget) == InterfaceInfoPanel:
            widget.overlay_panel.setGeometry(cols, rows, x, y) # retarded i know
            widget.overlay_panel.set_expand_index(expand_index)
            widget.update_info_panel()


def load(bartender):
    global stuff
    stuff = []
    with open(SAVE_FILENAME, 'r') as f: 
        # Loading data - completed researches
        bartender.w_checkbox_completed_researches.setCheckState(int(f.readline()))
        bartender.w_checkbox_completed_researches_times.setCheckState(int(f.readline()))
        cols, rows = int(f.readline()), int(f.readline())
        x, y = int(f.readline()), int(f.readline())
        expand_index = int(f.readline())
        stuff += [[cols, rows, x, y, expand_index]]

        # Researching bars
        bartender.w_checkbox_researches.setCheckState(int(f.readline()))
        bartender.w_checkbox_researches_show_bars.setCheckState(int(f.readline()))
        cols, rows = int(f.readline()), int(f.readline())
        x, y = int(f.readline()), int(f.readline())
        expand_index = int(f.readline())
        stuff += [[cols, rows, x, y, expand_index]]
        # Offscreen units
        widget = bartender.w_tabs_settings.widget(0)
        widget.w_text_name.setText(f.readline()[:-1])
        widget.w_checkbox_hidden.setCheckState(int(f.readline()))
        widget.w_checkbox_selected.setCheckState(int(f.readline()))
        widget.w_checkbox_selected_policy.setCheckState(int(f.readline()))
        widget.w_text_selected_min.setValue(int(f.readline()))
        widget.w_text_selected_max.setValue(int(f.readline()))
        widget.w_checkbox_monks_relic.setCheckState(int(f.readline()))
        widget.w_checkbox_monks_relic_policy.setCheckState(int(f.readline()))
        widget.w_text_monks_relic_min.setValue(int(f.readline()))
        widget.w_text_monks_relic_max.setValue(int(f.readline()))
        widget.w_checkbox_group1.setCheckState(int(f.readline()))
        widget.w_checkbox_group1_policy.setCheckState(int(f.readline()))
        widget.w_text_group1_min.setValue(int(f.readline()))
        widget.w_text_group1_max.setValue(int(f.readline()))
        widget.w_checkbox_group2.setCheckState(int(f.readline()))
        widget.w_checkbox_group2_policy.setCheckState(int(f.readline()))
        widget.w_text_group2_min.setValue(int(f.readline()))
        widget.w_text_group2_max.setValue(int(f.readline()))
        widget.w_checkbox_group3.setCheckState(int(f.readline()))
        widget.w_checkbox_group3_policy.setCheckState(int(f.readline()))
        widget.w_text_group3_min.setValue(int(f.readline()))
        widget.w_text_group3_max.setValue(int(f.readline()))
        widget.w_checkbox_group4.setCheckState(int(f.readline()))
        widget.w_checkbox_group4_policy.setCheckState(int(f.readline()))
        widget.w_text_group4_min.setValue(int(f.readline()))
        widget.w_text_group4_max.setValue(int(f.readline()))
        widget.w_checkbox_group5.setCheckState(int(f.readline()))
        widget.w_checkbox_group5_policy.setCheckState(int(f.readline()))
        widget.w_text_group5_min.setValue(int(f.readline()))
        widget.w_text_group5_max.setValue(int(f.readline()))
        widget.w_checkbox_group6.setCheckState(int(f.readline()))
        widget.w_checkbox_group6_policy.setCheckState(int(f.readline()))
        widget.w_text_group6_min.setValue(int(f.readline()))
        widget.w_text_group6_max.setValue(int(f.readline()))
        widget.w_checkbox_group7.setCheckState(int(f.readline()))
        widget.w_checkbox_group7_policy.setCheckState(int(f.readline()))
        widget.w_text_group7_min.setValue(int(f.readline()))
        widget.w_text_group7_max.setValue(int(f.readline()))
        widget.w_checkbox_group8.setCheckState(int(f.readline()))
        widget.w_checkbox_group8_policy.setCheckState(int(f.readline()))
        widget.w_text_group8_min.setValue(int(f.readline()))
        widget.w_text_group8_max.setValue(int(f.readline()))
        widget.w_checkbox_group9.setCheckState(int(f.readline()))
        widget.w_checkbox_group9_policy.setCheckState(int(f.readline()))
        widget.w_text_group9_min.setValue(int(f.readline()))
        widget.w_text_group9_max.setValue(int(f.readline()))
        widget.w_checkbox_group0.setCheckState(int(f.readline()))
        widget.w_checkbox_group0_policy.setCheckState(int(f.readline()))
        widget.w_text_group0_min.setValue(int(f.readline()))
        widget.w_text_group0_max.setValue(int(f.readline()))
        widget.w_checkbox_civilians.setCheckState(int(f.readline()))
        widget.w_checkbox_civilians_policy.setCheckState(int(f.readline()))
        widget.w_text_civilians_min.setValue(int(f.readline()))
        widget.w_text_civilians_max.setValue(int(f.readline()))
        widget.w_checkbox_military.setCheckState(int(f.readline()))
        widget.w_checkbox_military_policy.setCheckState(int(f.readline()))
        widget.w_text_military_min.setValue(int(f.readline()))
        widget.w_text_military_max.setValue(int(f.readline()))

        while True:
            widget_name = f.readline()
            if not widget_name:
                break
            name = f.readline()[:-1]
            if widget_name == "InterfaceBar\n":
                widget = InterfaceBar(name, bartender)
                bartender.w_tabs_settings.addTab(widget, name)
                widget.w_checkbox_aggregate.setCheckState(int(f.readline()))
                widget.w_checkbox_hidden.setCheckState(int(f.readline()))
                widget.w_text_idle_time_for_pulsing.setValue(int(f.readline()))
                widget.w_text_idle_time_for_blinkin.setValue(int(f.readline()))
                widget.w_combo_timer_number.setCurrentIndex(int(f.readline()))
                widget.w_combo_top_number.setCurrentIndex(int(f.readline()))
                widget.w_combo_top_number_aggr.setCurrentIndex(int(f.readline()))
                widget.w_combo_bottom_number.setCurrentIndex(int(f.readline()))
                widget.w_combo_bottom_number_aggr.setCurrentIndex(int(f.readline()))
                widget.w_checkbox_show_all_units.setCheckState(int(f.readline()))
                widget.w_checkbox_show_civilians.setCheckState(int(f.readline()))
                widget.w_checkbox_show_military.setCheckState(int(f.readline()))
                widget.w_checkbox_show_trade_units.setCheckState(int(f.readline()))
                widget.w_checkbox_show_fish_ships.setCheckState(int(f.readline()))
                widget.w_checkbox_show_villagers.setCheckState(int(f.readline()))
                widget.w_checkbox_show_food_vills.setCheckState(int(f.readline()))
                widget.w_checkbox_show_wood_vills.setCheckState(int(f.readline()))
                widget.w_checkbox_show_gold_vills.setCheckState(int(f.readline()))
                widget.w_checkbox_show_stone_vills.setCheckState(int(f.readline()))
                widget.w_checkbox_show_swordsmen.setCheckState(int(f.readline()))
                widget.w_checkbox_show_pikemen.setCheckState(int(f.readline()))
                widget.w_checkbox_show_eagles.setCheckState(int(f.readline()))
                widget.w_checkbox_show_huskarls.setCheckState(int(f.readline()))
                widget.w_checkbox_show_condottieros.setCheckState(int(f.readline()))
                widget.w_checkbox_show_light_cavalry.setCheckState(int(f.readline()))
                widget.w_checkbox_show_heavy_cavalry.setCheckState(int(f.readline()))
                widget.w_checkbox_show_camels.setCheckState(int(f.readline()))
                widget.w_checkbox_show_tarkans.setCheckState(int(f.readline()))
                widget.w_checkbox_show_battle_elephants.setCheckState(int(f.readline()))
                widget.w_checkbox_show_archers.setCheckState(int(f.readline()))
                widget.w_checkbox_show_skirmishers.setCheckState(int(f.readline()))
                widget.w_checkbox_show_cavalry_archers.setCheckState(int(f.readline()))
                widget.w_checkbox_show_genitours.setCheckState(int(f.readline()))
                widget.w_checkbox_show_hand_cannoneers.setCheckState(int(f.readline()))
                widget.w_checkbox_show_siege_rams.setCheckState(int(f.readline()))
                widget.w_checkbox_show_onagers.setCheckState(int(f.readline()))
                widget.w_checkbox_show_scorpions.setCheckState(int(f.readline()))
                widget.w_checkbox_show_bombard_cannons.setCheckState(int(f.readline()))
                widget.w_checkbox_show_siege_towers.setCheckState(int(f.readline()))
                widget.w_checkbox_show_war_ships.setCheckState(int(f.readline()))
                widget.w_checkbox_show_fire_ships.setCheckState(int(f.readline()))
                widget.w_checkbox_show_demolition_ships.setCheckState(int(f.readline()))
                widget.w_checkbox_show_cannon_galleons.setCheckState(int(f.readline()))
                widget.w_checkbox_show_unique_unit_ships.setCheckState(int(f.readline()))
                widget.w_checkbox_show_petards.setCheckState(int(f.readline()))
                widget.w_checkbox_show_trebuchets.setCheckState(int(f.readline()))
                widget.w_checkbox_show_unique_units.setCheckState(int(f.readline()))
                widget.w_checkbox_show_monks.setCheckState(int(f.readline()))
                widget.w_checkbox_show_transport_ships.setCheckState(int(f.readline()))
                widget.w_checkbox_show_all_buildings.setCheckState(int(f.readline()))
                widget.w_checkbox_show_town_centers.setCheckState(int(f.readline()))
                widget.w_checkbox_show_lumber_camps.setCheckState(int(f.readline()))
                widget.w_checkbox_show_mining_camps.setCheckState(int(f.readline()))
                widget.w_checkbox_show_mills.setCheckState(int(f.readline()))
                widget.w_checkbox_show_barracks.setCheckState(int(f.readline()))
                widget.w_checkbox_show_archery_ranges.setCheckState(int(f.readline()))
                widget.w_checkbox_show_stables.setCheckState(int(f.readline()))
                widget.w_checkbox_show_siege_workshops.setCheckState(int(f.readline()))
                widget.w_checkbox_show_monastries.setCheckState(int(f.readline()))
                widget.w_checkbox_show_castles.setCheckState(int(f.readline()))
                widget.w_checkbox_show_docks.setCheckState(int(f.readline()))
                widget.w_checkbox_show_blacksmiths.setCheckState(int(f.readline()))
                widget.w_checkbox_show_universities.setCheckState(int(f.readline()))
                widget.w_checkbox_show_markets.setCheckState(int(f.readline()))
                widget.w_checkbox_show_towers.setCheckState(int(f.readline()))
                widget.w_checkbox_show_slingers.setCheckState(int(f.readline()))
                widget.w_checkbox_show_livestock.setCheckState(int(f.readline()))
                widget.w_checkbox_show_gates.setCheckState(int(f.readline()))
                widget.w_checkbox_show_walls.setCheckState(int(f.readline()))
                widget.w_text_hp_min.setValue(int(f.readline()))
                widget.w_text_hp_max.setValue(int(f.readline()))
                widget.w_text_idle_min.setValue(int(f.readline()))
                widget.w_text_idle_max.setValue(int(f.readline()))
                widget.w_filter_training.setCheckState(int(f.readline()))
                widget.w_filter_researching.setCheckState(int(f.readline()))
                widget.w_filter_constucted.setCheckState(int(f.readline()))
                widget.w_filter_selected.setCheckState(int(f.readline()))
                widget.w_filter_group0.setCheckState(int(f.readline()))
                widget.w_filter_group1.setCheckState(int(f.readline()))
                widget.w_filter_group2.setCheckState(int(f.readline()))
                widget.w_filter_group3.setCheckState(int(f.readline()))
                widget.w_filter_group4.setCheckState(int(f.readline()))
                widget.w_filter_group5.setCheckState(int(f.readline()))
                widget.w_filter_group6.setCheckState(int(f.readline()))
                widget.w_filter_group7.setCheckState(int(f.readline()))
                widget.w_filter_group8.setCheckState(int(f.readline()))
                widget.w_filter_group9.setCheckState(int(f.readline()))
                cols, rows = int(f.readline()), int(f.readline())
                x, y = int(f.readline()), int(f.readline())
                expand_index = int(f.readline())
                stuff += [[cols, rows, x, y, expand_index]]
            elif widget_name == "InterfaceInfoPanel\n":
                widget = InterfaceInfoPanel(name, bartender)
                bartender.w_tabs_settings.addTab(widget, name)
                widget.w_checkbox_hidden.setCheckState(int(f.readline()))
                widget.w_checkbox_wood.setCheckState(int(f.readline()))
                widget.w_checkbox_food.setCheckState(int(f.readline()))
                widget.w_checkbox_gold.setCheckState(int(f.readline()))
                widget.w_checkbox_stone.setCheckState(int(f.readline()))
                widget.w_checkbox_fish.setCheckState(int(f.readline()))
                widget.w_checkbox_trade.setCheckState(int(f.readline()))
                widget.w_checkbox_resources.setCheckState(int(f.readline()))
                widget.w_checkbox_resources_carrying.setCheckState(int(f.readline()))
                widget.w_checkbox_idle_vills.setCheckState(int(f.readline()))
                widget.w_checkbox_idle_vills_time.setCheckState(int(f.readline()))
                widget.w_checkbox_farm_reseeds.setCheckState(int(f.readline()))
                widget.w_checkbox_relics.setCheckState(int(f.readline()))
                widget.w_checkbox_civilians.setCheckState(int(f.readline()))
                widget.w_checkbox_military.setCheckState(int(f.readline()))
                widget.w_checkbox_kd_units.setCheckState(int(f.readline()))
                widget.w_checkbox_kd_buildings.setCheckState(int(f.readline()))
                widget.w_checkbox_game_time.setCheckState(int(f.readline()))
                x, y = int(f.readline()), int(f.readline())
                w, h = int(f.readline()), int(f.readline())
                expand_index = int(f.readline())
                stuff += [[x, y, w, h, expand_index]]
                



if __name__ == '__main__':
    import bartender