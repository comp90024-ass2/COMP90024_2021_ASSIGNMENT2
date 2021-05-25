import React from "react";
import { Map, GeoJSON } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "./Map.css";
const UnemploymentMap = ({ areas }) => {
    const mapStyle = {
        fillColor: "white",
        weight: 1,
        color: "black",
        fillOpacity: 1,
    };

    const u_onEachArea = (area, layer) => {
        layer.options.fillColor = area.properties.color;

        const line = "require parameters";
        const name = area.properties.ADMIN;
        const src_B = area.properties.src_B;

        if (name != null && src_B != null) {
            layer.bindPopup(`${name} ${src_B}`);
        } else {
            layer.bindPopup(`${line}`);
        }
    };

    return (
        <Map style={{ height: "90vh" }} zoom={4} center={[-25, 140]}>
            <GeoJSON
                style={mapStyle}
                data={areas}
                onEachFeature={u_onEachArea}
            />
        </Map>
    );
};

export default UnemploymentMap;
