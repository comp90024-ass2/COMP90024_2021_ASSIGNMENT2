import papa from "papaparse";
import h_legendItems from "../entities/h_LegendItems";
import i_legendItems from "../entities/I_LegendItems";
import u_legendItems from "../entities/U_LegendItems";
import s_legendItems from "../entities/S_LegendItems";
//import { features } from "../data/countries.json";
import { features } from "../data/state/AUS_state.json";
import axios from "axios";
import request from '../utils/request';

class LoadTask {
  // different csv file is set here for different sections.
  // currently they are url form.
  h_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv";
  i_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv";
  u_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv";
  s_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv";

  setState = null;

  
  /* ------ Happiness ------ */
  h_load = (setState) => {
    this.setState = setState;
    const data = [
      {
          x: "VICTORIA",
          y: 51
      },
      {
          x: "NEW SOUTH WALES",
          y: 62
      },
      {
          x: "QUEENSLAND",
          y: 78
      },
      {
          x: "WESTERN AUSTRALIA",
          y: 1
      },
      {
          x: "SOUTHERN AUSTRALIA",
          y: 90
      },
      {
          x: "TASMANIA",
          y: 70
      },
      {
          x: "NORTHERN TERRITORY",
          y:70
      }
  ]
  const hobart = request.get('/twitter_re/_design/happiness/_view/city_lang?key=["Hobart","en"]', {})
  const melbourne = request.get('/twitter_re/_design/happiness/_view/city_lang?key=["Melbourne","en"]', {})
  const sydney = request.get('/twitter_re/_design/happiness/_view/city_lang?key=["Sydney","en"]', {})
  const adelaide = request.get('/twitter_re/_design/happiness/_view/city_lang?key=["Adelaide","en"]', {})
  const perth = request.get('/twitter_re/_design/happiness/_view/city_lang?key=["Perth","en"]', {})
  const darwin = request.get('/twitter_re/_design/happiness/_view/city_lang?key=["Darwin","en"]', {})
  const brisbane = request.get('/twitter_re/_design/happiness/_view/city_lang?key=["Brisbane","en"]', {})
  axios
        .all([hobart, melbourne, sydney, adelaide, perth, darwin, brisbane])
        .then(
            axios.spread((...responses) => {
                let city_list = ["TASMANIA", "VICTORIA", "NEW SOUTH WALES", "SOUTHERN AUSTRALIA", "WESTERN AUSTRALIA", "NORTHERN TERRITORY", "QUEENSLAND"]
                let data3 = []
                let index = 0
                responses.forEach(element => {

                    data3.push({
                        x: city_list[index],
                        y: element.data.rows[0].value[0]
                    })
                    index += 1
                });
                this.#h_processData(data3)
            }))
        .catch(error => {console.log(error)})

  };

  #h_processData = (areas) => {
    console.log(features)
    // console.log(areas[0]);
    for (let i = 0; i < features.length; i++) {
      const json_area = features[i];
      const csv_area = areas.find(
          (csv_area) => json_area.properties.nt_state_2 === csv_area.x 
          || json_area.properties.wa_state_2 === csv_area.x 
          || json_area.properties.qld_stat_2 === csv_area.x 
          || json_area.properties.vic_stat_2 === csv_area.x 
          || json_area.properties.nsw_stat_2 === csv_area.x
          || json_area.properties.sa_state_s === csv_area.x
          || json_area.properties.tas_state_s === csv_area.x
          
      );
      // console.log(csv_area)
      json_area.properties.B = 0;
      json_area.properties.str_B = 0;

      if (csv_area != null) {
        let B = Number(csv_area.y);
        json_area.properties.B = B;
        json_area.properties.str_B = this.#formatNumberWithCommas(
            B
        );
      }
      this.#h_setAreaColor(json_area);
    }

    this.setState(features);
  };

  #h_setAreaColor = (json_area) => {
    const h_legendItem = h_legendItems.find((item) =>
        item.isFor(json_area.properties.B)
    );

    if (h_legendItem != null) json_area.properties.color = h_legendItem.color;
  };

  /* ------ Income ------ */
  i_load = (setState) => {
    this.setState = setState;

    papa.parse(this.i_url, {
      download: true,
      header: true,
      complete: (result) => this.#i_processData(result.data),
    });
  };

  #i_processData = (areas) => {
    for (let i = 0; i < features.length; i++) {
      const json_area = features[i];
      const csv_area = areas.find(
          (csv_area) => json_area.properties.A === csv_area.A
      );

      json_area.properties.B = 0;
      json_area.properties.str_B = 0;

      if (csv_area != null) {
        let B = Number(csv_area.B);
        json_area.properties.B = B;
        json_area.properties.str_B = this.#formatNumberWithCommas(
            B
        );
      }
      this.#i_setAreaColor(json_area);
    }

    this.setState(features);
  };

  #i_setAreaColor = (json_area) => {
    const i_legendItem = i_legendItems.find((item) =>
        item.isFor(json_area.properties.B)
    );

    if (i_legendItem != null) json_area.properties.color = i_legendItem.color;
  };

  /* ------ Unemployment ------ */
  u_load = (setState) => {
    this.setState = setState;

    papa.parse(this.u_url, {
      download: true,
      header: true,
      complete: (result) => this.#u_processData(result.data),
    });
  };

  #u_processData = (areas) => {
    for (let i = 0; i < features.length; i++) {
      const json_area = features[i];
      const csv_area = areas.find(
          (csv_area) => json_area.properties.A === csv_area.A
      );

      json_area.properties.B = 0;
      json_area.properties.str_B = 0;

      if (csv_area != null) {
        let B = Number(csv_area.B);
        json_area.properties.B = B;
        json_area.properties.str_B = this.#formatNumberWithCommas(
            B
        );
      }
      this.#u_setAreaColor(json_area);
    }

    this.setState(features);
  };

  #u_setAreaColor = (json_area) => {
    const u_legendItem = u_legendItems.find((item) =>
        item.isFor(json_area.properties.B)
    );

    if (u_legendItem != null) json_area.properties.color = u_legendItem.color;
  };

  /* ------ Spent ------ */
  s_load = (setState) => {
    this.setState = setState;

    papa.parse(this.s_url, {
      download: true,
      header: true,
      complete: (result) => this.#s_processData(result.data),
    });
  };

  #s_processData = (areas) => {
    for (let i = 0; i < features.length; i++) {
      const json_area = features[i];
      const csv_area = areas.find(
          (csv_area) => json_area.properties.A === csv_area.A
      );

      json_area.properties.B = 0;
      json_area.properties.str_B = 0;

      if (csv_area != null) {
        let B = Number(csv_area.B);
        json_area.properties.B = B;
        json_area.properties.str_B = this.#formatNumberWithCommas(
            B
        );
      }
      this.#s_setAreaColor(json_area);
    }

    this.setState(features);
  };

  #s_setAreaColor = (json_area) => {
    const s_legendItem = s_legendItems.find((item) =>
        item.isFor(json_area.properties.B)
    );

    if (s_legendItem != null) json_area.properties.color = s_legendItem.color;
  };
  // common function call

  #formatNumberWithCommas = (number) => {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  };

}

export default LoadTask;
