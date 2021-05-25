import LegendItem from "./LengendItem";

var s_legendItems = [
    new LegendItem(
        "4,000 +",
        "#741f1f",
        (cases) => cases >= 4_000,
        "white"
    ),

    new LegendItem(
        "3,500 - 3,999",
        "#c57f7f",
        (cases) => cases >= 3_500 && cases < 4_000
    ),

    new LegendItem(
        "0 - 3,499",
        "#d8aaaa",
        (cases) => cases > 0 && cases < 3_500
    ),

    new LegendItem("No Data", "#ffffff", (cases) => true),

    new LegendItem("Average Spent:", "#f9f9f9", (cases) => true),
];

export default s_legendItems;

/**
 * 7 > 1 million                        #8b0000
 * 6 >= 500 thousand < 1 million        #9e2a2a
 * 5 >= 200 thousand < 500 thousand     #b15555
 * 4 >= 100 thousand  < 200 Thousand    #c57f7f
 * 3 > 50 thousand < 100 thousand       #d8aaaa
 * 2 >= 0 < 50 thousand                 #ebd4d4
 * 1 NO DATA                            #ffffff
 */

/*
#741f1f // Really red
#9c2929 // more red
#c57f7f // red
#d8aaaa //more pink
#ebd4d4 //pink
#ffffff //white
*/
