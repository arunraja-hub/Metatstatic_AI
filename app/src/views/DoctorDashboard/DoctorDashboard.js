import React from "react";
// @material-ui/core
import { makeStyles } from "@material-ui/core/styles";
import MUIDataTable from "mui-datatables";


import styles from "assets/jss/material-dashboard-react/views/dashboardStyle.js";
const axios = require('axios').default;

async function getPatient() {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/patientList');
      const myJson = await response.json();
      console.log(JSON.stringify(myJson));
      return JSON.parse(myJson);
    } catch (error) {
      console.error(error);
    }
}

const useStyles = makeStyles(styles);


const columns = [
  {
   name: "id",
   label: "Patient ID",
   options: {
    filter: true,
    sort: true,
   }
  },
  {
   name: "name",
   label: "Patient Name",
   options: {
    filter: true,
    sort: false,
   }
  },
  {
   name: "histologic_grade",
   label: "Histologic Grade",
   options: {
    filter: true,
    sort: true,
   }
  },
  {
   name: "ml_prediction",
   label: "ML Prediction",
   options: {
    filter: true,
    sort: true,
   }
  },
  {
    name: "pathology_report",
    label: "Pathology Report",
    options: {
     filter: true,
     sort: true,
    }
   },
   {
    name: "last_modified",
    label: "Last Modified",
    options: {
     filter: true,
     sort: true,
    }
   },
 ];
    
const options = {
  filterType: "dropdown",
  responsive: "scroll"
};

export default function Dashboard() {
  const classes = useStyles();
  //const data = getPatient();
  const data = [
    {
        "id": 1,
        "name": "Justin",
        "histologic_grade": 0,
        "ml_prediction": 0.0,
        "pathology_report": "HyperLink",
        "last_modified": "2019-10-31"
    },
    {
        "id": 2,
        "name": "Justin Ho",
        "histologic_grade": 0,
        "ml_prediction": 0.0,
        "pathology_report": "HyperLink",
        "last_modified": "2019-10-31"
    },
    {
        "id": 3,
        "name": "Arun",
        "histologic_grade": 1,
        "ml_prediction": 90.5,
        "pathology_report": "HyperLink",
        "last_modified": "2019-10-31"
    },
    {
        "id": 4,
        "name": "Justin",
        "histologic_grade": 2,
        "ml_prediction": 10.5,
        "pathology_report": "HyperLink",
        "last_modified": "2019-10-31"
    },
    {
        "id": 5,
        "name": "a",
        "histologic_grade": 1,
        "ml_prediction": 50.0,
        "pathology_report": "HyperLink",
        "last_modified": "2019-10-31"
    }
]
  return (
    <div>
    <MUIDataTable
        title={"Patient Record Table"}
        data={data}
        columns={columns}
        options={options}
      />

    </div>
  );
}
