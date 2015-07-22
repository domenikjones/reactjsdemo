var AppartementListing = React.createClass({
    getInitialState: function() {
        return {
            appartement: {
                title: "Some Title"
            },
            modal_content: null,
            gmap: null
        }
    },
    openModal: function(element) {
        var pk = $(element.target).data('pk');
        this.loadAppartementFromAPI(pk);
        console.log("openModal from AppartementListing: "+pk);
    },
    loadAppartementFromAPI: function(pk) {
        // query django apiv1 appartmentlist view
        var url = 'http://localhost:8000/en/apiv1/appartements/'+pk+"/";
        console.log("api url: "+url);
        $.ajax({
            url: url,
            dataType: 'json',
            success: function(data) {
                console.log("appartment data from ajax: "+data);
                this.showAppartementModal(data);
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(url, status, err.toString());
            }.bind(this)
        });
    },
    showAppartementModal: function(data){
        this.setState({appartement: data});
        this.setState({modal_content: this.setModalContent()});
        this.refs.modal.open();
        $('#appartment-tabs').tab('show'); // init bootstrap tabs
    },
    initGMap: function() {
        console.log("init google map");
    },
    destroyGMap: function() {
        console.log("destroy google map");
    },
    setModalContent: function(){
        var appartement = this.state.appartement;
        // bootstrap modal content
        return (
            <div>
                <div className="row">

                    <div className="title">
                        <h1>
                            {appartement.title}<br />
                            <small>{appartement.description}</small>
                        </h1>
                    </div>

                    <div className="tab-navigation">
                        <ul className="nav nav-tabs" id="appartment-tabs" role="tablist">
                            <li className="active" role="presentation"><a href="#overview" aria-controls="overview" role="tab" data-toggle="tab">Overview</a></li>
                            <li className="" role="presentation"><a href="#map" aria-controls="map" role="tab" data-toggle="tab">Show on Map</a></li>
                        </ul>
                    </div>

                    <div className="content">
                        <div className="tab-content">
                            <div role="tabpanel" className="tab-pane active" id="overview">
                                TAB OVERVIEW
                            </div>
                            <div role="tabpanel" className="tab-pane" id="map">
                                TAB MAP
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        );
        /*
        <div className="content">
            pk: {this.state.appartement.pk}<br />
            UUID: {this.state.appartement.uuid}<br /><br />
            Available: {this.state.appartement.available}<br />
            Living Space: {this.state.appartement.living_space}<br />
            Floor: {this.state.appartement.floor}<br />
            Balconies: {this.state.appartement.balconies}<br />
            Balconies Space: {this.state.appartement.balconies_space}<br />
            Price: {this.state.appartement.price}<br />
            Price Netto: {this.state.appartement.price_netto}<br />
            Street No.: {this.state.appartement.street_nr}<br />
            Postal Code: {this.state.appartement.postal_code}<br />
            City: {this.state.appartement.city}<br />
            Country: {this.state.appartement.country}<br /><br />
            Contact Name: {this.state.appartement.contact_name}<br />
            Contact Email: {this.state.appartement.contact_email}<br />
            Contact Phone: {this.state.appartement.contact_phone}<br />
        </div>
        */
    },
    render: function() {
        // create AppartementItems provided by api
        var AppartementItems = this.props.appartements.map(function(appartement){
            return (
                <div className="col-xs-12 col-sm-6 col-md-6 col-lg-4">
                    <div className="material-card">
                        <Appartement title={appartement.title}
                                     key={appartement.uuid}
                                     uuid={appartement.uuid}
                                     published_date_start={appartement.publish_date_start}
                                     published_date_end={appartement.publish_date_end}
                                     id={appartement.pk}
                                     data={appartement}
                                     onOpenModal={this.openModal}
                        />
                    </div>
                </div>
            );
        }, this);

        var AppartementModal = (
            <BootstrapModal ref="modal" confirm="OK" cancel="Cancel" title={this.state.appartement.title}>
            {this.state.modal_content}
            </BootstrapModal>
        );

        var show_results_class = "hidden";
        if(this.props.appartements.length > 0) {
            show_results_class = "";
        }
        var show_results_class_inverse = "";
        if(this.props.appartements.length > 0) {
            show_results_class_inverse = "hidden";
        }

        return (
            <div className="row">
                <div className="appartement-listing col-sm-12">

                    <div className={show_results_class}>
                        <div className="content-padding">
                            <h2>Results ({this.props.appartements.length})</h2>
                        </div>
                    </div>

                    <div className={show_results_class_inverse}>
                        <div className="content-padding">
                            No Results. Please refine your query filter.
                        </div>
                    </div>

                    <div>
                        {AppartementItems}
                        {AppartementModal}
                    </div>
                </div>
            </div>
        );
    }
});