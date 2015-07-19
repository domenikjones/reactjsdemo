/** @jsx React.DOM */
var SearchForm = React.createClass({
    propTypes: {
        onSubmit: React.PropTypes.func
    },
    getInitialState: function() {
        return {
            // initial form values
            form: {
                location: "",
                price_from: null,
                price_to: null,
                room_from: null,
                room_to: null,
                distance: null
            },
            form_helpers: {
                price_range: [null,100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 10000],
                room_range: [null,1,2,3,4,5,6,7,8,9,10],
                distance_range: [null,1,5,10,50,100],
                living_space_range: [null,10,20,30,40,50,60,70,80,90,100]
            }
        }
    },
    printFormData: function() {
        console.log("=== HANDLE FORM SUBMIT / CHANGE ===");
        console.log("form data (location): "+this.state.form.location);
        console.log("form data (price_from): "+this.state.form.price_from);
        console.log("form data (price_to): "+this.state.form.price_to);
        console.log("form data (room_from): "+this.state.form.room_from);
        console.log("form data (room_to): "+this.state.form.room_to);
        console.log("form data (distance): "+this.state.form.distance);
        console.log("form data (living_space_from): "+this.state.form.living_space_from);
        console.log("form data (living_space_to): "+this.state.form.living_space_to);
        console.log("=== END HANDLE FORM SUBMIT / CHANGE ===");
    },
    handleFormSubmit: function(e) {
        // call the parents (Demo) onSubmit callback
        console.log("handle form submit");
        this.setStateFormData();
        this.printFormData();
        if (typeof this.props.onSubmit === 'function') {
            this.props.onSubmit();
        }
    },
    handleFormChange: function(event) {
        console.log("handle form change");
        this.setStateFormData();
        this.printFormData();
    },
    setStateFormData: function() {
        this.state.form.location = this.refs.search_form_location.getDOMNode().value;
        this.state.form.price_from = this.refs.search_form_price_from.getDOMNode().value;
        this.state.form.price_to = this.refs.search_form_price_to.getDOMNode().value;
        this.state.form.room_from = this.refs.search_form_room_from.getDOMNode().value;
        this.state.form.room_to = this.refs.search_form_room_to.getDOMNode().value;
        this.state.form.distance = this.refs.search_form_distance.getDOMNode().value;
        this.state.form.living_space_from = this.refs.search_form_living_space_from.getDOMNode().value;
        this.state.form.living_space_to = this.refs.search_form_living_space_to.getDOMNode().value;
    },
    render: function() {
        var form_helpers = this.state.form_helpers;
        var price_range = form_helpers.price_range;
        var room_range = form_helpers.room_range;
        var distance_range = form_helpers.distance_range;
        var living_space_range = form_helpers.living_space_range;

        return (
            <div className="content-padding">

                <div className="row">
                    <div className="divider bottom"> </div>
                </div>

                <div ref="search_form" className="search-form">

                    <div className="row">

                        <div className="col-sm-12 col-sm-4 col-md-4 col-lg-3">
                            <div className="form-group">
                                <label>
                                    City*
                                    <input styles="color: black;" type="text" name="city" ref="search_form_location"
                                        className="form-control" onChange={this.handleFormChange} />
                                </label>
                            </div>
                        </div>


                        <div className="col-sm-6 col-sm-2 col-md-2  col-lg-1">
                            <div className="form-group">
                                <label>
                                    Distance*
                                    <div className="row">
                                        <div className="col-xs-12">
                                            <i className="fa fa-angle-down select-arrow"></i>
                                            <select name="price_from" ref="search_form_distance" id=""
                                                className="form-control" onChange={this.handleFormChange}>
                                                {distance_range.map(function(distance) {
                                                    return (
                                                        <option value={distance}>{distance}</option>
                                                    );
                                                })}
                                            </select>

                                        </div>
                                    </div>
                                </label>
                            </div>
                        </div>

                        <div className="col-sm-6 col-sm-4 col-md-4 col-lg-2">
                            <div className="form-group">
                                <label>
                                    Price (CHF)
                                    <div className="row">
                                        <div className="col-xs-6">
                                            <i className="fa fa-angle-down select-arrow"></i>
                                            <select name="price_from" ref="search_form_price_from" id=""
                                                className="form-control" onChange={this.handleFormChange}>
                                                {price_range.map(function(price) {
                                                    return (
                                                        <option value={price}>{price}</option>
                                                    );
                                                })}
                                            </select>
                                        </div>
                                        <div className="col-xs-6">
                                            <i className="fa fa-angle-down select-arrow"></i>
                                            <select name="price_to" ref="search_form_price_to" id=""
                                                className="form-control" onChange={this.handleFormChange}>
                                                {price_range.map(function(price) {
                                                    return (
                                                        <option value={price}>{price}</option>
                                                    );
                                                })}
                                            </select>
                                        </div>
                                    </div>
                                </label>
                            </div>
                        </div>

                        <div className="col-sm-6 col-sm-4 col-md-4 col-lg-2">
                            <div className="form-group">
                                <label>
                                    Rooms

                                    <div className="row">
                                        <div className="col-xs-6">
                                            <i className="fa fa-angle-down select-arrow"></i>
                                            <select name="room_from" ref="search_form_room_from" id=""
                                                className="form-control" onChange={this.handleFormChange}>
                                                {room_range.map(function(room) {
                                                    return (
                                                        <option value={room}>{room}</option>
                                                    );
                                                })}
                                            </select>
                                        </div>
                                        <div className="col-xs-6">
                                            <i className="fa fa-angle-down select-arrow"></i>
                                            <select name="room_to" ref="search_form_room_to" id=""
                                                className="form-control" onChange={this.handleFormChange}>
                                                {room_range.map(function(room) {
                                                    return (
                                                        <option value={room}>{room}</option>
                                                    );
                                                })}
                                            </select>
                                        </div>
                                    </div>

                                </label>
                            </div>
                        </div>

                        <div className="col-sm-6 col-sm-4 col-md-4 col-lg-2">
                            <div className="form-group">
                                <label>
                                    Living Space

                                    <div className="row">
                                        <div className="col-xs-6">
                                            <i className="fa fa-angle-down select-arrow"></i>
                                            <select name="room_from" ref="search_form_living_space_from" id=""
                                                className="form-control" onChange={this.handleFormChange}>
                                                {living_space_range.map(function(living_space) {
                                                    return (
                                                        <option value={living_space}>{living_space}</option>
                                                    );
                                                })}
                                            </select>
                                        </div>
                                        <div className="col-xs-6">
                                            <i className="fa fa-angle-down select-arrow"></i>
                                            <select name="room_to" ref="search_form_living_space_to" id=""
                                                className="form-control" onChange={this.handleFormChange}>
                                                {living_space_range.map(function(living_space) {
                                                    return (
                                                        <option value={living_space}>{living_space}</option>
                                                    );
                                                })}
                                            </select>
                                        </div>
                                    </div>

                                </label>
                            </div>
                        </div>

                        <div className="col-sm-12">

                            <div className="row">
                                <div className="col-sm-6 col-md-2">
                                    <div className="form-group">
                                        <span type="submit" value="Submit11" className="btn btn-material"
                                            onClick={this.handleFormSubmit}>
                                            Submit
                                        </span>
                                    </div>
                                </div>
                                <div className="col-sm-6">
                                    <br />
                                    <small>*these filters are still in development</small>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        );
    }
});