# Name to Date

A Python utility to update video and image file modification dates based on their filenames. This is particularly useful for Google Pixel phone media files, which have filenames like `PXL_20240813_051351918.mp4` or `PXL_20240815_174155846.NIGHT.jpg` containing the date and time when the media was recorded.

## Features

- Extracts date and time information from filenames in various formats (see Supported Filename Formats section)
- Updates the "Date Modified" attribute of media files to match the extracted datetime
- The datetime in filenames is assumed to be in UTC and it is for Google Pixel phones.
- Handles multiple file formats (`mp4`, `mov`, `avi`, `mkv`, `jpg`)

## Installation

### Prerequisites

- Python 3.6 or higher

### Installation from PyPI

```bash
pip install name2date
```

### Installation from Source

1. Clone this repository or download the source files
2. Navigate to the project directory
3. Install the package

```bash
pip install .
```

## Usage

### Basic Usage

After installation, you can use the command-line tool:

```bash
name2date /path/to/media
```

Alternatively, you can run the package as a module:

```bash
python -m name2date /path/to/media
```

This will process all supported media files (video and image) in the specified directory, extracting date and time from filenames and updating the "Date Modified" attribute. By default, the datetime is interpreted as UTC.

### Verbose Output

The tool supports two levels of verbosity:

```bash
name2date /path/to/media -v
```

This will print information only about skipped files (files that don't match the expected patterns).

```bash
name2date /path/to/media -vv
```

This will print detailed information about all files being processed, including which files are being processed and updated.

## Supported Filename Formats

The script is designed to work with various Google Pixel media filenames, which follow these patterns:

### PXL Format (with variations)

- `PXL_YYYYMMDD_HHMMSSXXX.mp4`
- `PXL_YYYYMMDD_HHMMSSXXX.NIGHT.jpg`
- `PXL_YYYYMMDD_HHMMSSXXX.MP.jpg`
- `PXL_YYYYMMDD_HHMMSSXXX.MP(N).jpg` (where N is a number)
- `PXL_YYYYMMDD_HHMMSSXXX(N).jpg` (where N is a number)
- `PXL_YYYYMMDD_HHMMSSXXX.RESTORED.jpg`
- `PXL_YYYYMMDD_HHMMSSXXX_exported_0_TIMESTAMP.jpg`

Where:
- `YYYY`: 4-digit year
- `MM`: 2-digit month (01-12)
- `DD`: 2-digit day (01-31)
- `HH`: 2-digit hour in 24-hour format (00-23)
- `MM`: 2-digit minute (00-59)
- `SS`: 2-digit second (00-59)
- `XXX`: 3-digit millisecond (000-999)

### LV Format

- `lv_0_YYYYMMDDHHMMSS.mp4`

Where:
- `YYYY`: 4-digit year
- `MM`: 2-digit month (01-12)
- `DD`: 2-digit day (01-31)
- `HH`: 2-digit hour in 24-hour format (00-23)
- `MM`: 2-digit minute (00-59)
- `SS`: 2-digit second (00-59)

Examples of supported filenames:
- `PXL_20240813_051351918.mp4`
- `PXL_20240815_174155846.NIGHT.jpg`
- `PXL_20240815_190034025.MP.jpg`
- `PXL_20240815_190407130(1).jpg`
- `PXL_20240815_190849820.RESTORED.jpg`
- `PXL_20240811_084139455_exported_0_1723365759303.jpg`
- `lv_0_20240813134545.mp4`

## Example
```shell
name2date -vv ~/Movies/gphoto
```
