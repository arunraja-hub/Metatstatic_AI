import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import PropTypes from "prop-types";
import { Card, CardBody, CardGroup, Col, Container, Row } from 'reactstrap';

import { getPatients, deletePatient } from '../../actions/index';

class Dashboard extends Component {

    // static propTypes = {
    //     patients: PropTypes.array.isRequired,
    //     getPatients: PropTypes.func.isRequired,
    //     deletePatient: PropTypes.func.isRequired,
    // };

    componentDidMount() {
        this.props.getPatients();
        console.log(this.props);
    }

    render() {
        return (
            <Fragment>
                    <h2>Patients</h2>
                    <table className="table table-striped">
                    <thead>
                        <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Histologic Grade</th>
                        <th>ML Prediction</th>
                        <th>Pathology Report</th>
                        <th>Last Modified</th>
                        <th />
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.patients.map(patient => (
                        <tr key={patient.id}>
                            <td>{patient.id}</td>
                            <td>{patient.name}</td>
                            <td>{patient.histologic_grade}</td>
                            <td>{patient.ml_prediction}</td>
                            <td>{patient.pathology_report}</td>
                            <td>{patient.last_modified}</td>
                            <td>
                            { <button
                                onClick={this.props.deletePatient.bind(this, patient.id)}
                                className="btn btn-danger btn-sm"
                            >
                                {" "}
                                Delete
                            </button> }
                            </td>
                        </tr>
                        ))}
                    </tbody>
                    </table>
            </Fragment>
        );
    }
}

Dashboard.propTypes = {
    patients: PropTypes.array.isRequired,
    getPatients: PropTypes.func.isRequired,
    deletePatient: PropTypes.func.isRequired,
};



const mapStateToProps = state => ({
    patients: state.patients.patients
});

export default (connect(mapStateToProps,{ getPatients, deletePatient })(Dashboard));
