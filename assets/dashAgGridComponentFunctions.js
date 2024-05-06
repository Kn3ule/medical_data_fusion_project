var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.Details = function (props) {
    return React.createElement(
        'a',
        {href: '/ecg-view/' + props.value},
        props.value
    );
};