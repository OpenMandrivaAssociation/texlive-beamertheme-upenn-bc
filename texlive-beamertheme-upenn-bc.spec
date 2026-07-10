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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-upenn-bc
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-upenn-bc
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-upenn-bc/README
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-upenn-bc/beamerBCstyle.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-upenn-bc/beamerBCstyle.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-upenn-bc/beamerPENNstyle.pdf
%{_datadir}/texmf-dist/tex/latex/beamertheme-upenn-bc/beamercolorthemegoeagles.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-upenn-bc/beamercolorthemepenn.sty
