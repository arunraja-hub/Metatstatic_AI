import React, { Fragment, useState } from 'react';
import Message from './Message';
import Progress from './Progress';
import axios from 'axios';



const FileUpload = () => {
    const [file, setFile] = useState('');
    const [filename, setFilename] = useState('Choose File');
    const [uploadedFile, setUploadedFile] = useState({});
    const [message, setMessage] = useState('');
    const [pathologyScanName, SetpathologyScanName] = useState('');
    const [uploadPercentage, setUploadPercentage] = useState(0);
  
    const onChange = e => {
      setFile(e.target.files[0]);
      setFilename(e.target.files[0].name);
    };

    const handleChange = (e) => {
        SetpathologyScanName(e.target.value);
    };
  
    const onSubmit = async e => {
      e.preventDefault();
      const formData = new FormData();
      formData.append('pathology_Main_Img', file);
      formData.append('name', "Patient Scan");
      formData.append('patient', 2);

  
      try {
        //const res = await axios.post('http://127.0.0.1:8000/api/pathologyScan/', formData, {
        const res = await axios.post('api/pathologyScan/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          onUploadProgress: progressEvent => {
            setUploadPercentage(
              parseInt(
                Math.round((progressEvent.loaded * 100) / progressEvent.total)
              )
            );
  
            // Clear percentage
            setTimeout(() => setUploadPercentage(0), 10000);
          }
        });

        const filePath = res.data.jpg_file;
        const fileName = res.data.name;
        const riskScore = res.data.ml_prediction;
  
        //const { fileName, filePath } = res.data;
  
        setUploadedFile({ fileName, filePath, riskScore });
  
        setMessage('File Uploaded');
      } catch (err) {
        if (err.response.status === 500) {
          setMessage('There was a problem with the server');
        } else {
          setMessage(err.response.data.msg);
        }
      }
    };
  
    return (
      <Fragment>
        {message ? <Message msg={message} /> : null}
        <form onSubmit={onSubmit}>
          <div className='custom-file mb-4'>
            <input
              type='file'
              className='custom-file-input'
              id='customFile'
              onChange={onChange}
            />
            <label className='custom-file-label' htmlFor='customFile'>
              {filename}
            </label>
          </div>
  
          <Progress percentage={uploadPercentage} />
  
          <input
            type='submit'
            value='Upload'
            className='btn btn-primary btn-block mt-4'
          />
        </form>
        {uploadedFile ? (
          <div className='row mt-5'>
            <div className='col-md-6 m-auto'>
              <h3 className='text-center'>{uploadedFile.fileName}</h3>
              <h3 className='text-center'>Risk Score: {uploadedFile.riskScore} %</h3>
              <img style={{ width: '100%' }} src={uploadedFile.filePath} alt='' />
            </div>
          </div>
        ) : null}
      </Fragment>
    );
  };
  
  export default FileUpload;