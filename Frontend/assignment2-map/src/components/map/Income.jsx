import React, { useState, useEffect } from "react";

import Loading from "./Loading";
import IncomeMap from "./IncomeMap";
import Legend from "./Legend";
import i_legendItems from "../../entities/I_LegendItems";
import LoadTask from "../../tasks/LoadTask";

const Income = () => {
    const [areas, setAreas] = useState([]);

    const legendItemsReverse = [...i_legendItems].reverse();

    const load = () => {
        const loadTask = new LoadTask();
        loadTask.i_load((areas) => setAreas(areas));
    };

    useEffect(load, []);

    return (
        <div>
            {areas.length === 0 ? (
                <Loading />
            ) : (
                <div>
                    <IncomeMap areas={areas} />
                    <Legend legendItems={legendItemsReverse} />
                </div>
            )}
        </div>
    );
};

export default Income;
