%global tl_name beamertheme-upenn-bc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Beamer themes for Boston College and the University of Pennsylvania
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/upenn-bc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-upenn-bc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-upenn-bc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Beamer themes in the colors of the University of Pennsylvania, USA, and
Boston College, USA. Both were tested for the presentation theme
'Warsaw'. Please note that these color themes are neither official nor
exact! The colours are approximated from the universities' style
guidelines and websites, and slightly modified where necessary to
generate an appealing look. The universities neither endorse, nor
provide any support for, these color themes. I give no warranty for the
code.

