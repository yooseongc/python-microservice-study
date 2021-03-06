var RacesBox = React.createClass({
  displayName: 'RacesBox',

  loadRacesFromServer: function () {
    var xhr = new XMLHttpRequest();
    xhr.open('get', this.props.url, true);
    xhr.onload = function () {
      var data = JSON.parse(xhr.responseText);
      this.setState({ data: data });
    }.bind(this);
    xhr.send();
  },

  getInitialState: function () {
    return { data: [] };
  },

  componentDidMount: function () {
    this.loadRacesFromServer();
  },

  render: function () {
    return React.createElement(
      'div',
      null,
      React.createElement(
        'h2',
        null,
        'Races'
      ),
      React.createElement(Races, { data: this.state.data })
    );
  }
});

var Races = React.createClass({
  displayName: 'Races',

  render: function () {
    var runNodes = this.props.data.map(function (run) {
      return React.createElement(Race, { title: run.title, type: run.type });
    });

    return React.createElement(
      'div',
      null,
      runNodes
    );
  }
});

// Here we decide what goes in a Thing node, which we defined above.
var Race = React.createClass({
  displayName: 'Race',

  render: function () {
    return React.createElement(
      'div',
      null,
      this.props.title,
      ' (',
      this.props.type,
      ')'
    );
  }
});
var RunsBox = React.createClass({
  displayName: 'RunsBox',

  loadRunsFromServer: function () {
    var xhr = new XMLHttpRequest();
    xhr.open('get', this.props.url, true);
    xhr.withCredentials = true;
    xhr.onload = function () {
      var data = JSON.parse(xhr.responseText);
      this.setState({ data: data });
    }.bind(this);
    xhr.send();
  },

  getInitialState: function () {
    return { data: [] };
  },

  componentDidMount: function () {
    this.loadRunsFromServer();
  },

  render: function () {
    return React.createElement(
      'div',
      null,
      React.createElement(
        'h2',
        null,
        'Runs'
      ),
      React.createElement(Runs, { data: this.state.data })
    );
  }
});

var Runs = React.createClass({
  displayName: 'Runs',

  render: function () {
    var runNodes = this.props.data.map(function (run) {
      return React.createElement(Run, { title: run.title, type: run.type });
    });

    return React.createElement(
      'div',
      null,
      runNodes
    );
  }
});

var Run = React.createClass({
  displayName: 'Run',

  render: function () {
    return React.createElement(
      'div',
      null,
      this.props.title,
      ' (',
      this.props.type,
      ')'
    );
  }
});

window.RunsBox = RunsBox;
var TrainingRunsBox = React.createClass({
  displayName: 'TrainingRunsBox',

  loadTrainingRunsFromServer: function () {
    var xhr = new XMLHttpRequest();
    xhr.open('get', this.props.url, true);
    xhr.onload = function () {
      var data = JSON.parse(xhr.responseText);
      this.setState({ data: data });
    }.bind(this);
    xhr.send();
  },

  getInitialState: function () {
    return { data: [] };
  },

  componentDidMount: function () {
    this.loadTrainingRunsFromServer();
  },

  render: function () {
    return React.createElement(
      'div',
      null,
      React.createElement(
        'h2',
        null,
        'TrainingRuns'
      ),
      React.createElement(TrainingRuns, { data: this.state.data })
    );
  }
});

var TrainingRuns = React.createClass({
  displayName: 'TrainingRuns',

  render: function () {
    var runNodes = this.props.data.map(function (run) {
      return React.createElement(TrainingRun, { title: run.title, type: run.type });
    });

    return React.createElement(
      'div',
      null,
      runNodes
    );
  }
});

// Here we decide what goes in a Thing node, which we defined above.
var TrainingRun = React.createClass({
  displayName: 'TrainingRun',

  render: function () {
    return React.createElement(
      'div',
      null,
      this.props.title,
      ' (',
      this.props.type,
      ')'
    );
  }
});
ReactDOM.render(React.createElement(RunsBox, { url: "/api/runs/2017/01" }), document.getElementById('runs'));

