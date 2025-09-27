# Partition: Automatic Layer Partitioning for YOLO Model

This project provides an automatic partitioning tool for the YOLO model, enabling efficient split inference across multiple devices or layers. The partitioning is based on cost and timing data, using Dijkstra's algorithm to find the optimal split points.

## Features

- **Automatic Partitioning:** Uses Dijkstra's algorithm to determine optimal layer splits.
- **Customizable Cost Functions:** Easily modify communication and computation costs.
- **Support for Multi-Layer Models:** Designed for models like YOLO with multiple layers.

## Project Structure

## Getting Started

### Prerequisites

- Python 3.8 or higher

### How to Run

1. Open a terminal in the project root directory.
2. Run the partitioning script:

   ```sh
   python src/dijkstra.py
   ```

### How to View Test Bed Data

To quickly view the current layer times and communication times used for partitioning, run:

```sh
python src/handle_data.py
```

This will print the values of `layer_times_2`, `layer_times_3`, `comm_times`, and the cost matrix to the console.  
You can use this to verify or debug your partitioning setup.
