import React, { Component } from 'react';
// Import React FilePond
import { FilePond, registerPlugin } from "react-filepond";
import PropTypes from 'prop-types';

// Import FilePond styles
import "filepond/dist/filepond.min.css";

// Import the Image EXIF Orientation and Image Preview plugins
// Note: These need to be installed separately
import FilePondPluginImageExifOrientation from "filepond-plugin-image-exif-orientation";
import FilePondPluginImagePreview from "filepond-plugin-image-preview";
import "filepond-plugin-image-preview/dist/filepond-plugin-image-preview.css";
import Gallery from 'react-grid-gallery';

import p1Image1 from "/media/jpg_images/images/1_Gw2UH6J.jpg";
import p1Image2 from "../../assets/patientImages/1/2.jpg";
import p1Image3 from "../../assets/patientImages/1/3.jpg";
import p2Image1 from "../../assets/patientImages/2/4.jpg";
import p2Image2 from "../../assets/patientImages/2/5.jpg";

// Register the plugins
registerPlugin(FilePondPluginImageExifOrientation, FilePondPluginImagePreview);
var patientOneID = "1";
var patientTwoID = "2";
var patientImagesDir = "../../assets/patientImages/";

class ImageAnalysis extends Component {
;
    constructor(props) {
        super(props);
    
        this.state = {
          // Set initial files, type 'local' means this is a file
          // that has already been uploaded to the server (see docs)
          files: [
            // {
            //   source: "index.html",
            //   options: {
            //     type: "local"
            //   }
            // }
          ],
          images : this.props.images
        };
    }
    
      handleInit() {
        console.log("FilePond instance has initialised", this.pond);
      }


    render() {
        return (
            <div className="animated fadeIn">
                {/* Pass FilePond properties as attributes */}
                <FilePond
                    ref={ref => (this.pond = ref)}
                    files={this.state.files}
                    allowMultiple={true}
                    maxFiles={3}
                    server="/api/pathologyScanUpload"
                    oninit={() => this.handleInit()}
                        onupdatefiles={fileItems => {
                        // Set currently active file objects to this.state
                        this.setState({
                            files: fileItems.map(fileItem => fileItem.file)
                        });
                    }}
                />
                <Gallery
                    images={this.state.images}
                    enableImageSelection={false}
                />
            </div>

        );
    }
}

ImageAnalysis.propTypes = {
  images: PropTypes.arrayOf(
      PropTypes.shape({
          src: PropTypes.string.isRequired,
          thumbnail: PropTypes.string.isRequired,
          srcset: PropTypes.array,
          caption: PropTypes.string,
          thumbnailWidth: PropTypes.number.isRequired,
          thumbnailHeight: PropTypes.number.isRequired,
          isSelected: PropTypes.bool
      })
  ).isRequired
};

ImageAnalysis.defaultProps = {
  images: [
      {
          src: p1Image1,
          thumbnail: p1Image1,
          thumbnailWidth: 100,
          thumbnailHeight: 100,
          thumbnailCaption: "80%"
      },
      {
          src: p1Image2,
          thumbnail: p1Image2,
          thumbnailWidth: 100,
          thumbnailHeight: 100,
          thumbnailCaption: "90%"
      },
      {
          src: p1Image3,
          thumbnail: p1Image3,
          thumbnailWidth: 100,
          thumbnailHeight: 100,
          thumbnailCaption: "70%"
      },
      {
          src: p2Image1,
          thumbnail: p2Image1,
          thumbnailWidth: 100,
          thumbnailHeight: 100,
          thumbnailCaption: "60%"
      },
      {
          src: p2Image2,
          thumbnail: p2Image2,
          thumbnailWidth: 100,
          thumbnailHeight: 100,
          thumbnailCaption: "50%"
      }
  ]
};

export default ImageAnalysis;
