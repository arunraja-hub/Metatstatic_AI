import React, { Component } from 'react';
import axios from 'axios';


class Page1 extends Component {

  state = {
    title: '',
    content: '',
    image: null
  };

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value
    })
  };

  handleImageChange = (e) => {
    this.setState({
      image: e.target.files[0]
    })
  };

  handleSubmit = (e) => {
    e.preventDefault();
    console.log(this.state);
    let form_data = new FormData();
    form_data.append('pathology_Main_Img', this.state.image, this.state.image.name);
    form_data.append('name', this.state.name);
    let url = 'http://localhost:8000/api/pathologyScan/';
    axios.post(url, form_data, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    })
        .then(res => {
          console.log(res.data);
        })
        .catch(err => console.log(err))
  };
    


    render() {
        return (
            <div className="animated fadeIn">
                <form onSubmit={this.handleSubmit}>
                  <p>
                    <input type="text" placeholder='Title' id='title' value={this.state.title} onChange={this.handleChange} required/>
                  </p>
                  <p>
                    <input type="text" placeholder='Content' id='content' value={this.state.content} onChange={this.handleChange} required/>
                  </p>
                  <p>
                    <input type="file"
                          id="image"
                          accept="image/png, image/jpeg"  onChange={this.handleImageChange} required/>
                  </p>
                    <input type="submit"/>
                 </form>
            </div>
        );
    }
}

export default Page1;
