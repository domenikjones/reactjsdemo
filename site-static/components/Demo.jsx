/** @jsx React.DOM */
var App = React.createClass({
    componentDidMount: function () {
        this.toggleLoader();
    },
    toggleLoader: function(){
        var loader = $('#loader');
        var wrapper = $('#wrapper');
        loader.removeClass('loaded');
        loader.addClass('unloaded');
        wrapper.removeClass('unloaded');
        wrapper.addClass('loaded');
    },
    render: function () {
        return (
            <Demo ref="demo" />
        )
    }
});

/*
Demo App
 */
var Demo = React.createClass({
    getInitialState: function() {
        return {
            appartements: [],
            paginator: {next: null, previous: null},
            page: 1,
            item: 0
        };
    },
    loadAppartementsFromAPI: function() {
        // query django apiv1 appartmentlist view
        $.ajax({
            url: 'http://localhost:8000/en/apiv1/appartementslist/?page='+this.state.page+
                "&"+$.param(this.refs.search_form.state.form),
            dataType: 'json',
            success: function(data) {
                this.setState({appartements: data.results});
                this.setPagination(data);
            }.bind(this),
            error: function(xhr, status, err) {
                console.error('http://localhost:8000/en/apiv1/appartementslist/', status, err.toString());
            }.bind(this)
        });
    },
    setPagination: function(data) {
        paginationArray = {
            next: null,
            prev: null
        };
        if (data.prev) {
            paginationArray['prev'] = data.prev;
        }
        if (data.next) {
            paginationArray['next'] = data.next;
        }
        this.setState({paginator: paginationArray})
    },
    setNewPage: function(int) {
        console.log("changePage: "+int);
        this.state.page = this.state.page + int;
        this.loadAppartementsFromAPI();
    },
    submitSearchForm: function() {
        this.loadAppartementsFromAPI();
    },
    componentDidMount: function() {
//        console.log("componentDidMount::" +
//            "demo: this.refs.demo.search_form\n"+ this.dumpDict(this.refs.search_form.state.form));
    },
    // render
    render: function() {
        return (
            <div>
                <div className="boxed">
                    <SearchForm ref="search_form" onSubmit={this.submitSearchForm} />
                    <div className="clear"></div>
                </div>
                <div className="divider"></div>
                <div className="content-padding">
                    <div className="row">
                        <AppartementListing appartements={this.state.appartements} />
                    </div>
                </div>

                <ul className="paginator">
                    {this.state.paginator.prev && "<li><span onClick={this.setNewPage(-1)}>Previous</span></li>"}
                    {this.state.paginator.next && "<li><span onClick={this.setNewPage(1)}>Next</span></li>"}
                </ul>
            </div>
        );
    },
    // misc helpers
    dumpDict: function(arr,level) {
        var dumped_text = "";
        if(!level) level = 0;

        //The padding given at the beginning of the line.
        var level_padding = "";
        for(var j=0;j<level+1;j++) level_padding += "    ";

        if(typeof(arr) == 'object') { //Array/Hashes/Objects
            for(var item in arr) {
                var value = arr[item];

                if(typeof(value) == 'object') { //If it is an array,
                    dumped_text += level_padding + "'" + item + "' ...\n";
                    dumped_text += this.dumpDict(value,level+1);
                } else {
                    dumped_text += level_padding + "'" + item + "' => \"" + value + "\"\n";
                }
            }
        } else { //Stings/Chars/Numbers etc.
            dumped_text = "===>"+arr+"<===("+typeof(arr)+")";
        }
        return dumped_text;
    }
});