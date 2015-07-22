/** @jsx React.DOM */
var FormSelect = React.createClass({
    render: function() {
        return (
            <div className="form-group">
                <label>
                    {this.props.label}
                    <div className="row">
                        <div className="col-xs-12">
                            <i className="fa fa-angle-down select-arrow"></i>

                            <select name={this.props.id} ref={this.props.ref} id={this.props.id}
                                className="form-control">
                                {this.props.options.map(function(option) {
                                    return (
                                        <option value={option}>{option}</option>
                                    );
                                })}
                            </select>

                        </div>
                    </div>
                </label>
            </div>
        )
    }
});