This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.


## JSON file format
**Note: each file has its unique column names in "properties" section**

For NT section: 
                "nt_state_": "2006-01-12Z",
                "nt_state_1": null,
                "nt_state_2": "NORTHERN TERRITORY",
                "nt_state_3": "NT"
               	*or*
                "nt_lga_sh":"2016-05-25Z",
                "nt_lga_s_1":null,
                "nt_lga_s_2":"EAST ARNHEM REGION",
                "nt_lga_s_3":"EAST ARNHEM",
                "nt_lga_s_4":null,
                "nt_lga_s_5":"7"

For VIC section: it is
                "vic_state_": "2006-01-12Z",
                "vic_state_1": null,
                "vic_state_2": "NORTHERN TERRITORY",
                "vic_state_3": "NT"
                *or*
                "vic_lga_sh":"2016-05-25Z",
                "vic_lga_s_1":null,
                "vic_lga_s_2":"EAST ARNHEM REGION",
                "vic_lga_s_3":"EAST ARNHEM",
                "vic_lga_s_4":null,
                "vic_lga_s_5":"7"

other files as follows...

**Aus_state.json file Structure**

{
	"features": [
		{
			"type": "Feature",
			"id": "xxxx_xxxxxxxx_xxxx_xxxx_xxxx_xxxxxxxxxxxx.x",
			"geometry": {
				"type": "MultiPolygon",
				"coordinates": [
					[
						[
							[ xxx.xxx,-xx.xxx ],
							[ xxx.xxx,-xx.xxx ],
							.
							.
							[ xxx.xxx,-xx.xxx ]
						]
					]
				]
			},
            "geometry_name": "geom",
            "properties": {
                "st_ply_pid": "3076",
                "dt_create": "2006-01-12Z",
                "dt_retire": null,
                "state_pid": "7",
                "nt_state_": "2006-01-12Z",
                "nt_state_1": null,
                "nt_state_2": "NORTHERN TERRITORY",
                "nt_state_3": "NT"
            }
		},
		.
		.
		.
	]
}

**source state level json file structure**

{
	"type": "FeatureCollection",
	"features": [
		{
			"type": "Feature",
			"id": "xxxx_xxxxxxxx_xxxx_xxxx_xxxx_xxxxxxxxxxxx.x",
			"geometry": {
				"type": "MultiPolygon",
				"coordinates": [
					[
						[
							[ xxx.xxx,-xx.xxx ],
							[ xxx.xxx,-xx.xxx ],
							.
							.
							.
						]
					]
				]
			},
            "geometry_name": "geom",
            "properties":{
                "st_ply_pid": "3076",
                "dt_create": "2006-01-12Z",
                "dt_retire": null,
                "state_pid": "7",
                "nt_state_": "2006-01-12Z",
                "nt_state_1": null,
                "nt_state_2": "NORTHERN TERRITORY",
                "nt_state_3": "NT"
            }
		},
        .
        .
        .	
	],
    "totalFeatures": 781,
    "numberMatched": 781,
    "numberReturned": 781,
    "timeStamp": "2021-05-18T11:14:38.935Z",
    "crs": {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:EPSG::4283"
        }
    }
}

**lga level json file structure**

{
    "type":"FeatureCollection",
    "features":[
        {
            "type":"Feature",
            "id":"ckan_225a1af2_9b93_4162_9fe6_11e165255942.1",
            "geometry":{
                "type":"MultiPolygon",
                "coordinates":[
                    [
                        [
                            [ xxx.xxxxxxxx,-xx.xxxxxxxx ],
                            [ xxx.xxxxxxxx,-xx.xxxxxxxx ],
                            .
                            .
                            .
                            [ xxx.xxxxxxxx,-xx.xxxxxxxx ]
                        ]
                    ]
                ]
            },
            "geometry_name":"geom",
            "properties":{
                "lg_ply_pid":"2178",
                "dt_create":"2016-05-25Z",
                "dt_retire":null,
                "lga_pid":"NT93",
                "nt_lga_sh":"2016-05-25Z",
                "nt_lga_s_1":null,
                "nt_lga_s_2":"EAST ARNHEM REGION",
                "nt_lga_s_3":"EAST ARNHEM",
                "nt_lga_s_4":null,
                "nt_lga_s_5":"7"
            }
        },
        .
        .
        .
    ],
    "totalFeatures":812,
    "numberMatched":812,
    "numberReturned":812,
    "timeStamp":"2021-05-18T11:44:38.173Z",
    "crs":{
        "type":"name",
        "properties":{
            "name":"urn:ogc:def:crs:EPSG::4283"
        }
    }
}

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

### Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

### Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

### Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

### Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

### `npm run build` fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify
