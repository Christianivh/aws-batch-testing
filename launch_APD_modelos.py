from enum import Enum
import argparse
import time

sleep_time = 5

enum_country = Enum(
    value='country',
    names=[
        ('BO', 10),
        ('CL', 11),
        ('CO', 12),
        ('CR', 13),
        ('DO', 14),
        ('EC', 15),
        ('GT', 16),
        ('MX', 17),
        ('PA', 18),
        ('PE', 19),
        ('PR', 20),
        ('SV', 21)
        ]
)


def launch_apd_modelos(cod_country, year_campaign_process):

    print('CodCountry: ', cod_country, ' YearCampaignProcess', str(year_campaign_process))

    print('Start: ', time.strftime('%I:%M:%S %p', time.localtime()))
    time.sleep(sleep_time*enum_country[cod_country].value)
    print('Finish: ', time.strftime('%I:%M:%S %p', time.localtime()))
    print('Sleep Time: ', sleep_time)
    print('Finish')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-pais', action='store', dest='pais',
                        help='Codigo de pais que va ser corrido')
    parser.add_argument('-proceso', action='store', dest='anoCampanaProcesso',
                        help='La fecha de processo de campana en formato YYYYMM')

    args = parser.parse_args()
    codeCountry = args.pais
    yearCampaignProcess = int(args.anoCampanaProcesso)
    launch_apd_modelos(cod_country=codeCountry, year_campaign_process=yearCampaignProcess)
