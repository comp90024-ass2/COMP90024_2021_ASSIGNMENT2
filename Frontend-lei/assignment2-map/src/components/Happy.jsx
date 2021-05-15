import React, { useState, useEffect } from "react";

import Loading from "./Loading";
import HappyMap from "./HappyMap";
import LoadCountriesTask from "../tasks/LoadCountriesTask";
import Legend from "./Legend";
import legendItems from "../entities/LegendItems";

const Happy19 = () => {
  const [countries, setCountries] = useState([]);

  const legendItemsReverse = [...legendItems].reverse();

  const load = () => {
    console.log("load");
    const loadCountriesTask = new LoadCountriesTask();
    loadCountriesTask.load((countries) => setCountries(countries));
  };

  useEffect(load, []);

  return (
    <div>
      {countries.length === 0 ? (
        <Loading />
      ) : (
        <div>
          <HappyMap countries={countries} />
          <Legend legendItems={legendItemsReverse} />
        </div>
      )}
    </div>
  );
};

export default Happy;
