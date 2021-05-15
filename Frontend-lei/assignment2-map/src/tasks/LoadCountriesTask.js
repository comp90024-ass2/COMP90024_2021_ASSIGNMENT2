import papa from "papaparse";
import legendItems from "../entities/LegendItems";
import { features } from "../data/countries.json";
//import { features } from "../data/australiaJson.json"
//    this.setState(features);

class LoadCountryTask {
  url =
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv";

  setState = null;

  load = (setState) => {
    this.setState = setState;

    papa.parse(this.url, {
      download: true,
      header: true,
      complete: (result) => this.#processData(result.data),
    });
  };

  #processData = (happyCountries) => {
    for (let i = 0; i < features.length; i++) {
      const country = features[i];
      //console.log(country);
      const happyCountry = happyCountries.find(
        (happyCountry) => country.properties.ISO_A3 === happyCountry.ISO3
      );

      country.properties.confirmed = 0;
      country.properties.confirmedText = 0;

      if (happyCountry != null) {
        let confirmed = Number(happyCountry.Confirmed);
        country.properties.confirmed = confirmed;
        country.properties.confirmedText = this.#formatNumberWithCommas(
          confirmed
        );
      }
      this.#setCountryColor(country);
    }

    this.setState(features);
  };

  #setCountryColor = (country) => {
    const legendItem = legendItems.find((item) =>
      item.isFor(country.properties.confirmed)
    );

    if (legendItem != null) country.properties.color = legendItem.color;
  };

  #formatNumberWithCommas = (number) => {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  };
}

export default LoadCountryTask;
