import React, { useState, useEffect } from "react";

import Loading from "./Loading";
import HappyMap from "./HappyMap";
import LoadTask from "../../tasks/LoadTask";
import Legend from "./Legend";
import h_legendItems from "../../entities/H_LegendItems";
import {Map} from "react-leaflet";

const Happy = () => {
  const [areas, setAreas] = useState([]);

  const legendItemsReverse = [...h_legendItems].reverse();

  const load = () => {
    const loadTask = new LoadTask();
    loadTask.h_load((areas) => setAreas(areas));
  };

  useEffect(load, []);

  return (
    <div>
      {areas.length === 0 ? (
        <Loading />
      ) : (
        <div>
          <HappyMap areas={areas} />
          <Legend legendItems={legendItemsReverse} />
        </div>
      )}
    </div>
  );
};

export default Happy;
