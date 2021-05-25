import React, { useState, useEffect } from "react";

import Loading from "./Loading";
import SpentMap from "./SpentMap";
import Legend from "./Legend";
import s_legendItems from "../../entities/S_LegendItems";
import LoadTask from "../../tasks/LoadTask";

const Spent = () => {
    const [areas, setAreas] = useState([]);

    const legendItemsReverse = [...s_legendItems].reverse();

    const load = () => {
        const loadTask = new LoadTask();
        loadTask.s_load((areas) => setAreas(areas));
    };

    useEffect(load, []);

    return (
        <div>
            {areas.length === 0 ? (
                <Loading />
            ) : (
                <div>
                    <SpentMap areas={areas} />
                    <Legend legendItems={legendItemsReverse} />
                </div>
            )}
        </div>
    );
};

export default Spent;
