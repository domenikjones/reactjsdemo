/** @jsx React.DOM */
var Appartement = React.createClass({
    propTypes: {
        onOpenModal: React.PropTypes.func
    },
    handleCollapseClass: function(element) {
        console.log("handleCollapseClass: "+element);
    },
    clickOpenModal: function(e) {
        if (typeof this.props.onOpenModal === 'function') {
            this.props.onOpenModal(e);
        }
    },
    render: function() {
        var uniqueKey = "appartement_"+this.props.data.pk;
        var uniqueDetailesCollapseString = "collpaseDetailedInformation_"+this.props.data.pk;
        var uniqueDetailesCollapseStringHash = "#collpaseDetailedInformation_"+this.props.data.pk;
        var data = this.props.data;

        var background_url = "url('"+this.props.data.main_image_url+"') center center;";

        return (
            <div className="appartement" key={uniqueKey}>

                <div onClick={this.clickOpenModal} data-pk={data.pk}
                    className="cover" style={{background: background_url}}></div>

                <div className="title">
                    <h2>
                        <span onClick={this.clickOpenModal} data-pk={data.pk}>{data.title}</span>
                    </h2>
                </div>

                <div className="container-fluid">
                    <div className="row">
                        <div className="col-xs-12 col-sm-8">
                            {this.props.data.street_nr}<br />
                            {this.props.data.city}, {this.props.data.postal_code}<br />
                        </div>
                        <div className="col-xs-12 col-sm-4">
                            <div className="align-right">
                                <strong>CHF {this.props.data.price}</strong><br />
                                <small>
                                    {this.props.data.rooms} Rooms<br />
                                    {this.props.data.living_space} m<span className="superscript">2</span>
                                </small>
                            </div>
                        </div>
                    </div>
                    <br />
                </div>

                <div className="description" style={{display: "none"}}>
                    <span className="" data-toggle="collapse" data-target={uniqueDetailesCollapseStringHash}
                        aria-expanded="false" aria-controls={uniqueDetailesCollapseString}
                        onClick={this.handleCollapseClass}>
                        <span>Detailed information</span><br />
                    </span>

                    <div className="collapse" id={uniqueDetailesCollapseString}>
                        <span>UUID: {this.props.uuid}</span><br />
                        Pusblished From: <span>{this.props.published_date_start}</span><br />
                        Pubslished To: <span>{this.props.published_date_end}</span><br />
                    </div>
                </div>

            </div>
        );

//        {this.props.data.main_image && <img src={this.props.data.main_image} />}
//        {this.props.data.main_image_url && <img src={this.props.data.main_image_url} />}
    }
});