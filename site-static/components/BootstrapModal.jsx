/** @jsx React.DOM */
var BootstrapModal = React.createClass({
    propTypes: {
        appartement: {
            title: null
        }
    },
    getInitialState: function() {
        return {
            appartement: {
                title: null
            }
        }
    },
    // The following two methods are the only places we need to
    // integrate with Bootstrap or jQuery!
    componentDidMount: function () {
        // When the component is added, turn it into a modal
        $(this.getDOMNode()).modal({backdrop: true, keyboard: true, show: false})
    },
    componentWillUnmount: function () {
        $(this.getDOMNode()).off('hidden', this.handleHidden);
    },
    close: function () {
        $(this.getDOMNode()).modal('hide');
    },
    open: function () {
        $(this.getDOMNode()).modal('show');
    },
    handleClose: function() {
        this.close();
    },
    render: function () {
        return (
            <div className="modal fade">
                <div className="container modal-container">

                    <div className="modal-header">
                        <button
                            type="button"
                            className="close"
                            onClick={this.handleClose}
                            dangerouslySetInnerHTML={{__html: '&times'}}
                        />
                        <h3>{this.props.title}</h3>
                    </div>

                    <div className="modal-body">
                        {this.props.children}
                    </div>

                </div>
            </div>
        );
    }
});