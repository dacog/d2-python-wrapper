# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project tries to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2024-11-22

### Added

- Dark theme support with `dark_theme` parameter
- Sketch mode rendering with `sketch` parameter
- SVG centering with `center` parameter
- Output scaling with `scale` parameter
- SVG asset bundling control with `bundle` parameter
- Tooltip appendix forcing with `force_appendix` parameter
- Execution timeout control with `timeout` parameter
- Board animation with `animate_interval` parameter
- Target board specification with `target` parameter
- Custom font support:
  - Regular font with `font_regular`
  - Italic font with `font_italic`
  - Bold font with `font_bold`
  - Semibold font with `font_semibold`

### Changed

- Improved type hints using `Union` and `Literal` types

### Fixed

- 

## [0.1.0] - Initial Release

### Added

- Basic D2 diagram rendering support
- Multiple output formats (svg, png, pdf)
- Theme customization
- Layout engine options
- Platform detection and binary management
