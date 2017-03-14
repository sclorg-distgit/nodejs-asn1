%{?scl:%scl_package nodejs-asn1}
%{!?scl:%global pkg_name %{name}}

%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-asn1
Version:        0.2.3
Release:        1%{?dist}
Summary:        Contains parsers and serializers for ASN.1 (currently BER only)
BuildArch:      noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
License:        MIT
URL:            https://github.com/mcavage/node-asn1
Source0:        http://registry.npmjs.org/asn1/-/asn1-%{version}.tgz
BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(tap)
%endif

%description
nodejs-asn1 is a library for encoding and decoding Abstract Syntax Notation One
(ASN.1) datatypes in pure JavaScript. ASN.1 is  is a standard and notation that 
describes rules and structures for representing, encoding, transmitting, and 
decoding data in telecommunications and computer networking.

Currently Basic Encoding Rules (BER) encoding is supported; at some point 
Distinguished Encoding Rules (DER) will likely also be supported.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/asn1
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/asn1

%nodejs_symlink_deps

%if 0%{enable_tests}
%check
%nodejs_symlink_deps --check
tap ./tst
%endif

%files
%{nodejs_sitelib}/asn1
%doc LICENSE README.md

%changelog
* Tue Sep 06 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.2.3-1
- Update

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.11-5.1
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.11-4.1
- Rebuilt with updated metapackage

* Wed Dec 11 2013 Tomas Hrcka <thrcka@redhat.com> - 0.1.11-3.1
- enable scl support

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-3
- restrict to compatible arches

* Fri Jun 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-2
- improve description

* Thu Jun 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-1
- initial package
