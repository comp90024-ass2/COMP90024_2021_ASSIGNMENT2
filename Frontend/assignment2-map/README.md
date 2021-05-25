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

For NT section: <br />
                "nt_state_": "2006-01-12Z",<br />
                "nt_state_1": null,<br />
                "nt_state_2": "NORTHERN TERRITORY",<br />
                "nt_state_3": "NT"<br />
               	*or*<br />
                "nt_lga_sh":"2016-05-25Z",<br />
                "nt_lga_s_1":null,<br />
                "nt_lga_s_2":"EAST ARNHEM REGION",<br />
                "nt_lga_s_3":"EAST ARNHEM",<br />
                "nt_lga_s_4":null,<br />
                "nt_lga_s_5":"7"<br />

For VIC section: <br />
                "vic_state_": "2006-01-12Z",<br />
                "vic_state_1": null,<br />
                "vic_state_2": "NORTHERN TERRITORY",<br />
                "vic_state_3": "NT"<br />
                *or*<br />
                "vic_lga_sh":"2016-05-25Z",<br />
                "vic_lga_s_1":null,<br />
                "vic_lga_s_2":"EAST ARNHEM REGION",<br />
                "vic_lga_s_3":"EAST ARNHEM",<br />
                "vic_lga_s_4":null,<br />
                "vic_lga_s_5":"7"<br />

other files as follows...

**Aus_state.json file Structure**

{<br />
	"features": [<br />
		{<br />
			"type": "Feature",<br />
			"id": "xxxx_xxxxxxxx_xxxx_xxxx_xxxx_xxxxxxxxxxxx.x",<br />
			"geometry": {<br />
				"type": "MultiPolygon",<br />
				"coordinates": [<br />
					[<br />
						[<br />
							[ xxx.xxx,-xx.xxx ],<br />
							[ xxx.xxx,-xx.xxx ],<br />
							.<br />
							.<br />
							[ xxx.xxx,-xx.xxx ]<br />
						]<br />
					]<br />
				]<br />
			},<br />
            "geometry_name": "geom",<br />
            "properties": {<br />
                "st_ply_pid": "3076",<br />
                "dt_create": "2006-01-12Z",<br />
                "dt_retire": null,<br />
                "state_pid": "7",<br />
                "nt_state_": "2006-01-12Z",<br />
                "nt_state_1": null,<br />
                "nt_state_2": "NORTHERN TERRITORY",<br />
                "nt_state_3": "NT"<br />
            }<br />
		},<br />
		.<br />
		.<br />
		.<br />
	]<br />
}<br />

**source state level json file structure**

{<br />
	"type": "FeatureCollection",<br />
	"features": [<br />
		{<br />
			"type": "Feature",<br />
			"id": "xxxx_xxxxxxxx_xxxx_xxxx_xxxx_xxxxxxxxxxxx.x",<br />
			"geometry": {<br />
				"type": "MultiPolygon",<br />
				"coordinates": [<br />
					[<br />
						[<br />
							[ xxx.xxx,-xx.xxx ],<br />
							[ xxx.xxx,-xx.xxx ],<br />
							.<br />
							.<br />
							.<br />
						]<br />
					]<br />
				]<br />
			},<br />
            "geometry_name": "geom",<br />
            "properties":{<br />
                "st_ply_pid": "3076",<br />
                "dt_create": "2006-01-12Z",<br />
                "dt_retire": null,<br />
                "state_pid": "7",<br />
                "nt_state_": "2006-01-12Z",<br />
                "nt_state_1": null,<br />
                "nt_state_2": "NORTHERN TERRITORY",<br />
                "nt_state_3": "NT"<br />
            }<br />
		},<br />
        .<br />
        .<br />
        .<br />
	],<br />
    "totalFeatures": 781,<br />
    "numberMatched": 781,<br />
    "numberReturned": 781,<br />
    "timeStamp": "2021-05-18T11:14:38.935Z",<br />
    "crs": {<br />
        "type": "name",<br />
        "properties": {<br />
            "name": "urn:ogc:def:crs:EPSG::4283"<br />
        }<br />
    }<br />
}<br />

**lga level json file structure**

{<br />
    "type":"FeatureCollection",<br />
    "features":[<br />
        {<br />
            "type":"Feature",<br />
            "id":"ckan_225a1af2_9b93_4162_9fe6_11e165255942.1",<br />
            "geometry":{<br />
                "type":"MultiPolygon",<br />
                "coordinates":[<br />
                    [<br />
                        [<br />
                            [ xxx.xxxxxxxx,-xx.xxxxxxxx ],<br />
                            [ xxx.xxxxxxxx,-xx.xxxxxxxx ],<br />
                            .<br />
                            .<br />
                            .<br />
                            [ xxx.xxxxxxxx,-xx.xxxxxxxx ]<br />
                        ]<br />
                    ]<br />
                ]<br />
            },<br />
            "geometry_name":"geom",<br />
            "properties":{<br />
                "lg_ply_pid":"2178",<br />
                "dt_create":"2016-05-25Z",<br />
                "dt_retire":null,<br />
                "lga_pid":"NT93",<br />
                "nt_lga_sh":"2016-05-25Z",<br />
                "nt_lga_s_1":null,<br />
                "nt_lga_s_2":"EAST ARNHEM REGION",<br />
                "nt_lga_s_3":"EAST ARNHEM",<br />
                "nt_lga_s_4":null,<br />
                "nt_lga_s_5":"7"<br />
            }<br />
        },<br />
        .<br />
        .<br />
        .<br />
    ],<br />
    "totalFeatures":812,<br />
    "numberMatched":812,<br />
    "numberReturned":812,<br />
    "timeStamp":"2021-05-18T11:44:38.173Z",<br />
    "crs":{<br />
        "type":"name",<br />
        "properties":{<br />
            "name":"urn:ogc:def:crs:EPSG::4283"<br />
        }<br />
    }<br />
}<br />

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
