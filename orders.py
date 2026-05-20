# SECURE: Using SQLAlchemy ORM filtering
@app.route('/api/orders')
@login_required
def get_orders():
    status_filter = request.args.get('status', 'pending')
    # The ORM automatically parameterizes the inputs safely
    orders = Order.query.filter_by(status=status_filter, user_id=current_user.id).all()
    return jsonify([order.to_dict() for order in orders])