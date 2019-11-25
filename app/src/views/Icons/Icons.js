/*eslint-disable*/
import React from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import Hidden from "@material-ui/core/Hidden";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardBody from "components/Card/CardBody.js";

import styles from "assets/jss/material-dashboard-react/views/iconsStyle.js";
import Gallery from 'react-grid-gallery';

const IMAGES = 
[ 
  {
    src: "http://127.0.0.1:8000/static/1.jpg",
    thumbnail : "http://127.0.0.1:8000/static/1.jpg",
    thumbnailWidth: 60,
    thumbnailHeight: 60
  }
];

const useStyles = makeStyles(styles);

export default function Icons() {
  const classes = useStyles();
  const IMAGES = 
  [ 
    {
      src: "http://127.0.0.1:8000/static/1.jpg",
      thumbnail : "http://127.0.0.1:8000/static/1.jpg",
      thumbnailWidth: 60,
      thumbnailHeight: 60
    },
    {
      src: "http://127.0.0.1:8000/static/2.jpg",
      thumbnail : "http://127.0.0.1:8000/static/2.jpg",
      thumbnailWidth: 60,
      thumbnailHeight: 60
    }
  ]
  return (
    <div>
      <Gallery images={IMAGES}/>
    </div>
    
    
  );
}
