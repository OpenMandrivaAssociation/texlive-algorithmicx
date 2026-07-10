%global tl_name algorithmicx
%global tl_revision 78101

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The algorithmic style you always wanted
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/algorithmicx
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithmicx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithmicx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Algorithmicx provides a flexible, yet easy to use, way for inserting
good looking pseudocode or source code in your papers. It has built in
support for Pseudocode, Pascal and C, and offers powerful means to
create definitions for any programming language. The user can adapt a
Pseudocode style to his native language.

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
%dir %{_datadir}/texmf-dist/doc/latex/algorithmicx
%dir %{_datadir}/texmf-dist/tex/latex/algorithmicx
%doc %{_datadir}/texmf-dist/doc/latex/algorithmicx/README
%doc %{_datadir}/texmf-dist/doc/latex/algorithmicx/algorithmicx.pdf
%doc %{_datadir}/texmf-dist/doc/latex/algorithmicx/algorithmicx.tex
%{_datadir}/texmf-dist/tex/latex/algorithmicx/algc.sty
%{_datadir}/texmf-dist/tex/latex/algorithmicx/algcompatible.sty
%{_datadir}/texmf-dist/tex/latex/algorithmicx/algmatlab.sty
%{_datadir}/texmf-dist/tex/latex/algorithmicx/algorithmicx.sty
%{_datadir}/texmf-dist/tex/latex/algorithmicx/algpascal.sty
%{_datadir}/texmf-dist/tex/latex/algorithmicx/algpseudocode.sty
