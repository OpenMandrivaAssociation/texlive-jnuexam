%global tl_name jnuexam
%global tl_revision 71883

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2024F
Release:	%{tl_revision}.1
Summary:	Exam class for Jinan University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jnuexam
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jnuexam.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jnuexam.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an exam class for Jinan University (China).

