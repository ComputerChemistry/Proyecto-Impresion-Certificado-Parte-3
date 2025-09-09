{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python313Full               
    pkgs.python313Packages.numpy     # numpy
    pkgs.python313Packages.pandas    # pandas
    pkgs.python313Packages.pillow    # Pillow
    pkgs.python313Packages.reportlab # reportlab
    pkgs.python313Packages.openpyxl # reportlab
    pkgs.python313Packages.pypdf
    pkgs.zlib                        # dependencia de compresión
    pkgs.libjpeg                     # imágenes
    pkgs.freetype                    # fuentes
  ];
}

