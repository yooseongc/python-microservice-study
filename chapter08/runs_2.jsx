
var RunsBox = React.createClass({
    loadRunsFromServer: function() {
        var xhr = new XMLHttpRequest();
        xhr.open("get", this.props.url, true);
        xhr.withCredentials = true;
        xhr.onload = function() {
            var data = JSON.parse(xhr.responseText);
            this.setState({ data: data });
        }.bind(this);
        xhr.send();
    },
    getInitialState: function() {
        return { data: [] };
    },
    componentDidMount: function() {
        this.loadRunsFromServer();
    },
    render: function() {
        return (
            <div>
                <h2>Runs</h2>
                <Runs data={ this.state.data } />
            </div>
        );
    }
});

window.RunsBox = RunsBox;