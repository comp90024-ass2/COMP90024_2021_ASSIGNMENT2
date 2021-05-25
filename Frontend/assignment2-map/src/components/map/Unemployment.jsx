import React, { useState, useEffect } from "react";

import Loading from "./Loading";
import UnemploymentMap from "./UnemploymentMap";
import Legend from "./Legend";
import u_legendItems from "../../entities/U_LegendItems";
import LoadTask from "../../tasks/LoadTask";

const Unemployment = () => {
    const [areas, setAreas] = useState([]);

    const legendItemsReverse = [...u_legendItems].reverse();

    const load = () => {
        const loadTask = new LoadTask();
        loadTask.u_load((areas) => setAreas(areas));
    };

    useEffect(load, []);

    return (
        <div>
            {areas.length === 0 ? (
                <Loading />
            ) : (
                <div>
                    <UnemploymentMap areas={areas} />
                    <Legend legendItems={legendItemsReverse} />
                </div>
            )}
        </div>
    );
};

export default Unemployment;
