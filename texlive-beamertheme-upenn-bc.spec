Name:		texlive-beamertheme-upenn-bc
Version:	29937
Release:	2
Summary:	Beamer themies for Boston College and the University of Pennsylvania
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/upenn-bc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-upenn-bc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-upenn-bc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Beamer themes in the colors of the - University of
Pennsylvania, USA, and - Boston College, USA. Both were tested
for the presentation theme 'Warsaw. Please note that these
color themes are neither official nor exact! The colours are
approximated from the universities' style guidelines and
websites, and slightly modified where necessary to generate an
appealing look. The universities neither endorse, nor provide
any support for, these color themes. I give no warranty for the
code.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beamertheme-upenn-bc/beamercolorthemegoeagles.sty
%{_texmfdistdir}/tex/latex/beamertheme-upenn-bc/beamercolorthemepenn.sty
%doc %{_texmfdistdir}/doc/latex/beamertheme-upenn-bc/README
%doc %{_texmfdistdir}/doc/latex/beamertheme-upenn-bc/beamerBCstyle.pdf
%doc %{_texmfdistdir}/doc/latex/beamertheme-upenn-bc/beamerBCstyle.tex
%doc %{_texmfdistdir}/doc/latex/beamertheme-upenn-bc/beamerPENNstyle.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
