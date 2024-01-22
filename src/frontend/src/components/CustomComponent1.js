import React from 'react';
import { API_BASE_URL, THEME_SETTINGS } from '../../utils/constants';
import './CustomComponent1.css';

class CustomComponent1 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      modelResponse: null,
      isLoading: false,
      error: null,
    };
  }

  componentDidMount() {
    this.fetchModelResponse();
  }

  fetchModelResponse = async () => {
    this.setState({ isLoading: true });
    try {
      const response = await fetch(`${API_BASE_URL}/model-response`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      this.setState({ modelResponse: data, isLoading: false });
    } catch (error) {
      this.setState({ error: error.message, isLoading: false });
    }
  };

  render() {
    const { modelResponse, isLoading, error } = this.state;

    return (
      <div id="custom-component-1" style={THEME_SETTINGS}>
        {isLoading && <p>Loading model response...</p>}
        {error && <p>Error fetching model response: {error}</p>}
        {modelResponse && (
          <div>
            <h2>Model Response</h2>
            <p>{modelResponse.text}</p>
          </div>
        )}
      </div>
    );
  }
}

export default CustomComponent1;