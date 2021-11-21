from booking.booking import Booking


# inst = Booking()
# inst.land_first_page()

with Booking() as bot:
    bot.land_first_page()
    # print("Exiting...")
    bot.change_currency(currency='USD')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2021-11-21',
                     check_out_date='2021-11-25')
    bot.select_adults(1)
    bot.click_search()
    bot.apply_filtrations()



